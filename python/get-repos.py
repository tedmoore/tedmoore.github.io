import requests
import tomli

# Replace 'USERNAME' with the GitHub username you want
username = "tedmoore"
url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"

# Make the GET request
response = requests.get(url)

# Check for errors
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.json())
else:
    repos = response.json()
    for repo in repos:
        for k in ['name', 'html_url', 'description', 'updated_at', 'language']:
            print(f"{k}: {repo.get(k)}")
        print("\n---\n")
        
# Load config.toml to check existing repos
with open("config.toml", "rb") as f:
    config = tomli.load(f)

existing_repos = [repo.get("name") for repo in config.get("params", {}).get("repos", [])]
print("Existing repos in config.toml:")
for repo in existing_repos:
    print(f" - {repo}")