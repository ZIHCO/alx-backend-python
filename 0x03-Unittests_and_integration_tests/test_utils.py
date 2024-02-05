#!/usr/bin/env python3
"""Module contains the TestAccessNestedMap"""
from unittest import TestCase
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
    """test case for utils.access_nested_map"""
    @parameterized.expand([
                           ({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                          ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
                           ({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                          ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """test case for get_json"""
    @parameterized.expand([
                           ("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                          ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)
        mock_requests_get.reset_mock()
