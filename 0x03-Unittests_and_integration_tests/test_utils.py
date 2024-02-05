#!/usr/bin/env python3
"""Module contains the TestAccessNestedMap"""
from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized


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
