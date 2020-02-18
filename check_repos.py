"""
Author: JoeyIsZY
"""

import requests
import json


def get_github_repos(github_user_id):
    repository = {}
    user_repos =requests.get(f'https://api.github.com/users/{github_user_id}/repos')
    parsed_user_repos = json.loads(user_repos.text)

    for repo in parsed_user_repos:
        repo_name = repo["name"]

        repo_commits = requests.get(f'https://api.github.com/repos/{github_user_id}/{repo_name}/commits')
        repo_commit = json.loads(repo_commits.text)

        repository[repo_name] = len(repo_commit)
        print(f'Repo: {repo_name} Number of commits: {len(repo_commit)}')

    return repository


if __name__ == '__main__':
    get_github_repos('JoeyIsZY')




