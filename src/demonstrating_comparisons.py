import requests

# Configuration
OWNER = 'itamargithub'
REPO = 'commits_compare_demo'
TOKEN = os.getenv('GITHUB_TOKEN')  # Use an environment variable for the token

# Headers for authentication
headers = {'Authorization': f'token {TOKEN}'}

def get_latest_commit(owner, repo, branch='main'):
    """Get the latest commit from a specific branch."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}'
    response = requests.get(url, headers=headers)
    commits = response.json()
    return commits[0] if commits else None

def get_single_commit(owner, repo, commit_sha):
    """Get a single commit's details."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'
    response = requests.get(url, headers=headers)
    return response.json()

def compare_two_commits(owner, repo, base_sha, head_sha):
    """Compare two specific commits."""
    url = f'https://api.github.com/repos/{owner}/{repo}/compare/{base_sha}...{head_sha}'
    response = requests.get(url, headers=headers)
    return response.json()

def print_commit_details(commit):
    """Print details of a single commit in a human-readable format."""
    print(f"Commit SHA: {commit['sha']}")
    print(f"Author: {commit['commit']['author']['name']} ({commit['commit']['author']['email']})")
    print(f"Date: {commit['commit']['author']['date']}")
    print(f"Message: {commit['commit']['message']}\n")

def print_comparison_details(comparison):
    """Print details of a comparison between two commits."""
    print(f"Base SHA: {comparison['base_commit']['sha']}")
    print(f"Head SHA: {comparison['merge_base_commit']['sha']}")
    print(f"Total Commits: {comparison['total_commits']}")
    if comparison['status'] != 'identical':
        print(f"Files Changed: {len(comparison['files'])}")
        print("Changes:")
        for file in comparison['files'][:5]:  # Print only first 5 changes for brevity
            print(f"  {file['filename']} - additions: {file['additions']} deletions: {file['deletions']}")
    else:
        print("No changes between the commits.")

# Example usage
if __name__ == "__main__":
    # Get the latest commit from main
    print("Fetching the latest commit from main...")
    main_commit = get_latest_commit(OWNER, REPO, 'main')
    print_commit_details(main_commit)

    # Get the latest commit from feature-branch
    print("Fetching the latest commit from feature-branch...")
    feature_commit = get_latest_commit(OWNER, REPO, 'feature-branch')
    print_commit_details(feature_commit)

    # Compare the latest commits of main and feature-branch
    if main_commit and feature_commit:
        print("Comparing the latest commits between main and feature-branch...")
        comparison = compare_two_commits(OWNER, REPO, main_commit['sha'], feature_commit['sha'])
        print_comparison_details(comparison)

