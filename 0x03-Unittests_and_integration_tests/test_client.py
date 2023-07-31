#!/usr/bin/env python3
"""test_client module
"""
import unittest
import fixtures
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from urllib.error import HTTPError
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """test_org function.
        Tests that GithubOrgClient.org returns the correct value.
        """
        test_class = GithubOrgClient(test_org_name)
        expected_url = f"https://api.github.com/orgs/{test_org_name}"
        test_class.org()
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """test_public_repos_url function.
        Tests that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value={"repos_url": "test_url"})):
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url, "test_url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test_public_repos function.
        Tests that the list of repos is what you expect from the chosen payload
        """
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   PropertyMock(return_value="test_url")):
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["Google", "Twitter"])
            mock_get_json.assert_called_once_with("test_url")

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    @patch('client.get_json')
    def test_has_license(self, repo, license_key, expected, mock_get_json):
        """test_has_license function.
        Tests that the result of has_license is the expected one
        based on the mocked payload.
        """
        with patch.object(GithubOrgClient, 'has_license') as mock_has_license:
            mock_has_license.return_value = expected
            self.assertEqual(GithubOrgClient.has_license(
                repo,
                license_key), expected)
            mock_has_license.assert_called_once_with(repo, license_key)


@parameterized_class([
    {"org_payload": fixtures.TEST_PAYLOAD[0][0],
     "repos_payload": fixtures.TEST_PAYLOAD[0][1],
     "expected_repos": fixtures.TEST_PAYLOAD[0][2],
     "apache2_repos": fixtures.TEST_PAYLOAD[0][3]},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class
    """

    @classmethod
    def setUpClass(cls, mock_get_json):
        """setUpClass method.
        """
        cls.get_patcher = patch('requests.get')
        cls.get_patcher.start()
        mock_get_json.side_effect = [
            cls.org_payload, cls.repos_payload, cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """tearDownClass method.
        """
        cls.get_patcher.stop()

    def test_public_repos(self, mock_get_json):
        """test_public_repos function.
        Tests that the list of repos is what you expect from the chosen payload
        """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("test"), [])
        mock_get_json.assert_called()

    def test_public_repos_with_license(self, mock_get_json):
        """test_public_repos_with_license function.
        Tests that the list of repos is what you expect from the chosen payload
        """
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        mock_get_json.assert_called()


if __name__ == '__main__':
    unittest.main()
