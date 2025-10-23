from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
import tomli
from jinja2 import Environment, FileSystemLoader


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT_DIR / "config.toml"
RESEARCH_PAGE_PATH = ROOT_DIR / "content" / "research" / "_index.md"
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
TEMPLATE_NAME = "selected_software.md.j2"
CACHE_DIR = Path(__file__).resolve().parent / ".cache"
CACHE_PATH = CACHE_DIR / "github_repos.json"

START_MARKER = "<!-- GENERATED_SELECTED_SOFTWARE:start -->"
END_MARKER = "<!-- GENERATED_SELECTED_SOFTWARE:end -->"
DEFAULT_GITHUB_OWNER = "tedmoore"


def load_research_configs() -> List[Dict[str, object]]:
    with open(CONFIG_PATH, "rb") as file_handle:
        config = tomli.load(file_handle)
    params = config.get("params", {})
    return list(params.get("research", []))


def create_github_session() -> requests.Session:
    session = requests.Session()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "personal-website-selected-software-script",
    }
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    session.headers.update(headers)
    return session


def parse_repo_coordinates(repo_config: Dict[str, object]) -> Optional[Tuple[str, str]]:
    gh_name = repo_config.get("gh_name")
    if not isinstance(gh_name, str) or not gh_name.strip():
        return None
    if "/" in gh_name:
        owner, repo = gh_name.split("/", 1)
        return owner.strip(), repo.strip()
    owner = repo_config.get("gh_owner")
    owner_name = owner if isinstance(owner, str) and owner.strip() else DEFAULT_GITHUB_OWNER
    return owner_name, gh_name.strip()


def fetch_repo_metadata(session: requests.Session, owner: str, repo: str) -> Dict[str, object]:
    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = session.get(repo_url, timeout=15)
    except requests.RequestException as error:
        print(f"⚠️  Unable to reach GitHub for {owner}/{repo}: {error}")
        return {}

    if response.status_code != 200:
        print(f"⚠️  GitHub returned {response.status_code} for {owner}/{repo}")
        return {}

    data = response.json()
    metadata: Dict[str, object] = {
        "full_name": data.get("full_name") or f"{owner}/{repo}",
        "html_url": data.get("html_url"),
        "description": data.get("description"),
        "stars": data.get("stargazers_count", 0) or 0,
        "is_fork": data.get("fork", False),
        "license": None,
    }

    license_info = data.get("license") or {}
    if isinstance(license_info, dict):
        metadata["license"] = license_info.get("name")

    parent_info = data.get("parent")
    if isinstance(parent_info, dict):
        metadata["fork_source"] = {
            "full_name": parent_info.get("full_name"),
            "html_url": parent_info.get("html_url"),
        }

    languages = fetch_repo_languages(session, owner, repo)
    metadata["languages"] = languages
    metadata["language_summary"] = summarize_github_languages(languages)
    return metadata


def fetch_repo_languages(session: requests.Session, owner: str, repo: str) -> Dict[str, int]:
    languages_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    try:
        response = session.get(languages_url, timeout=15)
    except requests.RequestException as error:
        print(f"⚠️  Unable to fetch languages for {owner}/{repo}: {error}")
        return {}

    if response.status_code != 200:
        return {}
    data = response.json()
    if isinstance(data, dict):
        return {key: value for key, value in data.items() if isinstance(key, str) and isinstance(value, int)}
    return {}


def load_cache() -> Dict[str, Dict[str, object]]:
    if not CACHE_PATH.exists():
        return {}
    try:
        with open(CACHE_PATH, "r", encoding="utf-8") as cache_file:
            data = json.load(cache_file)
            if isinstance(data, dict):
                return data
    except (json.JSONDecodeError, OSError) as error:
        print(f"⚠️  Unable to read cache: {error}")
    return {}


def save_cache(cache: Dict[str, Dict[str, object]]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as cache_file:
        json.dump(cache, cache_file, indent=2, sort_keys=True)


def get_repo_metadata(session: requests.Session, owner: str, repo: str, cache: Dict[str, Dict[str, object]]) -> Dict[str, object]:
    cache_key = f"{owner}/{repo}"
    metadata = fetch_repo_metadata(session, owner, repo)
    if metadata:
        cache[cache_key] = metadata
        return metadata

    cached_metadata = cache.get(cache_key)
    if cached_metadata:
        print(f"ℹ️  Using cached GitHub data for {cache_key}")
        return cached_metadata

    return {}


def summarize_github_languages(github_languages: Dict[str, int]) -> Optional[str]:
    if not github_languages:
        return None

    total = sum(github_languages.values())
    if total <= 0:
        return None
    ordered = sorted(github_languages.items(), key=lambda item: item[1], reverse=True)
    parts: List[str] = []
    for language, count in ordered:
        percentage = (count / total) * 100
        if percentage >= 1:
            parts.append(f"{language} {percentage:.0f}%")
    if not parts:
        return None
    return "💻 " + " · ".join(parts)


def combine_language_data(
    config_languages: Optional[object],
    github_languages: Dict[str, int],
    cached_summary: Optional[object],
) -> Optional[str]:
    combined: List[str] = []

    if github_languages:
        github_summary = summarize_github_languages(github_languages)
        if github_summary:
            combined.append(github_summary)
        seen_languages = set(github_languages)
    else:
        seen_languages = set()
        if isinstance(cached_summary, str) and cached_summary.strip():
            combined.append(cached_summary.strip())

    if isinstance(config_languages, list):
        extra_languages = [
            language
            for language in config_languages
            if isinstance(language, str) and language and language not in seen_languages
        ]
        if extra_languages:
            extras = " · ".join(extra_languages)
            combined.append(extras)

    if not combined:
        return None

    return " · ".join(combined)


def build_entry(
    repo_config: Dict[str, object], session: requests.Session, cache: Dict[str, Dict[str, object]]
) -> Dict[str, object]:
    owner_repo = parse_repo_coordinates(repo_config)
    github_data: Dict[str, object] = {}
    if owner_repo:
        owner, repo = owner_repo
        github_data = get_repo_metadata(session, owner, repo, cache)

    title = repo_config.get("title")
    title_text = title if isinstance(title, str) and title.strip() else None
    if not title_text:
        if github_data.get("full_name"):
            title_text = str(github_data["full_name"]).split("/", 1)[-1]
        elif owner_repo:
            title_text = owner_repo[1]
        else:
            title_text = "Untitled"

    description = repo_config.get("description")
    if not isinstance(description, str) or not description.strip():
        description = github_data.get("description") if github_data else None

    local_page = repo_config.get("local_page")
    local_page_text = local_page if isinstance(local_page, str) and local_page.strip() else None

    details: List[str] = []

    if local_page_text:
        title_text = f"[{title_text}]({local_page_text})"

    github_url = github_data.get("html_url") if github_data else None
    if not github_url and owner_repo:
        owner, repo = owner_repo
        github_url = f"https://github.com/{owner}/{repo}"

    if github_url:
        full_name = github_data.get("full_name") or ("/".join(owner_repo) if owner_repo else None)
        github_line = f"🐙 [GitHub Repo]({github_url})"
        stars = github_data.get("stars")
        if isinstance(stars, int) and stars > 0:
            github_line += f" {stars}⭐️"
        fork_source = github_data.get("fork_source") if github_data else None
        if isinstance(fork_source, dict):
            fork_name = fork_source.get("full_name")
            fork_url = fork_source.get("html_url")
            if fork_name and fork_url:
                github_line += f" / 🍴 from [{fork_name}]({fork_url})"
        details.append(github_line)

    github_languages_raw = github_data.get("languages") if github_data else None
    if isinstance(github_languages_raw, dict):
        github_languages = {
            key: value
            for key, value in github_languages_raw.items()
            if isinstance(key, str) and isinstance(value, int)
        }
    else:
        github_languages = {}
    cached_summary = github_data.get("language_summary") if github_data else None
    languages = combine_language_data(repo_config.get("languages"), github_languages, cached_summary)
    if languages:
        details.append(f" {languages}")

    license_name = repo_config.get("license")
    if not isinstance(license_name, str) or not license_name.strip():
        license_name = github_data.get("license") if github_data else None
    if isinstance(license_name, str) and license_name.strip():
        details.append(f"🛡 {license_name}")

    return {
        "title": title_text,
        "description": description,
        "details": details,
    }


def render_entries(entries: List[Dict[str, object]]) -> str:
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)
    template = env.get_template(TEMPLATE_NAME)
    rendered = template.render(entries=entries)
    return rendered.strip()


def update_research_page(rendered_block: str) -> None:
    content = RESEARCH_PAGE_PATH.read_text(encoding="utf-8")
    start_index = content.find(START_MARKER)
    end_index = content.find(END_MARKER)

    if start_index == -1 or end_index == -1 or end_index < start_index:
        raise RuntimeError("Required markers not found in research index page.")

    before = content[: start_index + len(START_MARKER)]
    after = content[end_index:]

    new_section = f"{before}\n\n{rendered_block}\n\n{after.lstrip()}"
    RESEARCH_PAGE_PATH.write_text(new_section, encoding="utf-8")


def main() -> None:
    research_configs = load_research_configs()
    if not research_configs:
        raise RuntimeError("No research repositories found in config.toml")

    session = create_github_session()
    cache = load_cache()
    entries = [build_entry(repo_config, session, cache) for repo_config in research_configs]
    rendered = render_entries(entries)
    update_research_page(rendered)
    save_cache(cache)


if __name__ == "__main__":
    main()
