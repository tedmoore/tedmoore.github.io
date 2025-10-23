import requests
import tomli

def add_repo(repo_config):
    print(f"processing - {repo_config.get('gh_name')}")
    url = f"https://api.github.com/repos/tedmoore/{repo_config.get('gh_name')}"
    # Make the GET request
    response = requests.get(url)

    # Check for errors
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.json())
    else:
        response_data = response.json()
        # print(response_data)
        for key, value in response_data.items():
            print(f"{key}: {value}")

# Load config.toml to check existing repos
with open("config.toml", "rb") as f:
    config = tomli.load(f)

repos = config.get('params').get("research")

for repo in repos:
    add_repo(repo)
