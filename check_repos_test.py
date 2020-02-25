import os
import unittest
import json
from check_repos import get_github_repos, get_github_repo_commits
from unittest.mock import patch


class RepoTestCase(unittest.TestCase):
    def test_get_github_repos(self):
        mock_get_github_repos_patcher = patch('check_repos.get_github_repos')
        mock_get_github_repos = mock_get_github_repos_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/repos.json') as file:
            mock_get_github_repos.return_value = json.load(file)
        mock_get_github_repos_patcher.stop()
        repo = mock_get_github_repos()

        mock_get_github_repo_commits_patcher = patch('check_repos.get_github_repo_commits')
        mock_get_github_repo_commits = mock_get_github_repo_commits_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/repos-commits.json') as file:
            mock_get_github_repo_commits.return_value = json.load(file)
        mock_get_github_repo_commits.stop()
        repo_commits = mock_get_github_repo_commits()

        self.assertEqual(len(repo_commits), 7)
        self.assertEqual(repo[0].get("full_name"), 'JoeyIsZY/555')
        self.assertEqual(repo_commits[0].get('node_id'), 'MDY6Q29tbWl0MjQxMjc2MTA5Ojg3Y2MxNmQ1NjBmOTExOTRiNDU1MzVhMDhlY2Y1ZTFlOTI0MmZhOWQ=')


if __name__ == '__main__':
    unittest.main()
