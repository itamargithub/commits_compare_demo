# src/compare_commits.py

import requests

def compare_commits(owner, repo, base, head, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/compare/{base}...{head}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
if __name__ == "__main__":
    owner = 'itamargithub'  # Your GitHub username
    repo = 'commits_compare_demo'
    base = 'main'  # The default branch or any other base commit
    head = 'feature-branch'  # Change this to the branch you want to compare
    TOKEN = os.getenv('GITHUB_TOKEN')  # Use an environment variable for the token  # Securely fetch/configure your GitHub token
    result = compare_commits(owner, repo, base, head, token)
    print(result)