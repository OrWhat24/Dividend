import os

def push_to_github(commit_message):
    github_token = os.getenv('GITHUB_TOKEN')  # Fetch the token from the environment variable
    if github_token is None:
        print("Error: GitHub token not found in environment variables.")
        return

    # Add GitHub token to remote URL
    os.system('git add .')
    os.system(f'git commit -m "{commit_message}"')
    os.system(f'git push https://{github_token}@github.com/OrWhat24/Dividend.git')
    print("Files successfully pushed to GitHub.")

# Example usage
push_to_github("Updated stock charts and data")

