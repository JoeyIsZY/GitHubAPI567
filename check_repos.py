"""
Author: JoeyIsZY
"""

import requests


def get_github_repos(github_user_id):
    user_repos =requests.get(f'https://api.github.com/users/{github_user_id}/repos')
    return user_repos


def get_github_repo_commits(github_user_id, repo_name):
    repo_commits = requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits')
    return repo_commits





