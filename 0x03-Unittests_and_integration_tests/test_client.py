#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""
import sys
import os
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value and calls get_json"""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected value from org property"""
        payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list and calls dependencies once"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload
        test_url = "https://api.github.com/orgs/testorg/repos"

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            client = GithubOrgClient("testorg")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)