import unittest
import json
import requests
from check_repos import get_github_repos


class RepoTestCase(unittest.TestCase):
    def test_get_github_repos(self):
        expected ={'555': 1, 'ip_adress': 2, 'ssw555tmHogwarts2020Spring': 20, 'SSW567': 4, 'SSW810': 3, 'test': 2, 'Triangle567': 9}

        self.assertEqual(get_github_repos('JoeyIsZY'), expected)


if __name__ == '__main__':
    unittest.main()
