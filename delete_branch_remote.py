from datetime import datetime, timedelta
from github import Github

def delete_old_branches(repository, max_age_minutes, protected_branches):
    branches = repository.get_branches()
    main_branches = [branch.name for branch in branches if branch.name in protected_branches]

    for branch in branches:
        if branch.name not in main_branches:
            last_commit = branch.commit.commit.author.date
            age = datetime.utcnow() - last_commit
            age_minutes = age.total_seconds() / 60

            if max_age_minutes <= age_minutes <= 15:
                print(f"Deleting branch {branch.name}...")
                repository.get_git_ref(f"heads/{branch.name}").delete()
                branch.edit(branch.name, branch.commit.sha, force=True)
                print(f"Branch {branch.name} deleted successfully.\n")

def main():
    # Replace 'your_access_token' and 'your_repository' with your GitHub access token and repository name.
    access_token = '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'
    repo_name = 'C:\\Users\IT\Desktop\python_del\.git'

    # Create a GitHub instancegit
    g = Github(access_token)

    # Get the repository
    repo = g.get_repo(repo_name)

    # Define protected branches (e.g., main, master, developer)
    protected_branches = ['main', 'master', 'developer']

    # Set the maximum age for branches to be deleted (in minutes)
    max_age_minutes = 5

    # Delete old branches
    delete_old_branches(repo, max_age_minutes, protected_branches)

if __name__ == "__main__":
    main()
