#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class
    """
    test_cases = [
        {
            "name": "nested_map",
            "nested_map": {"a": 1},
            "path": ("a",),
            "expected": 1
        },
        {
            "name": "nested_map",
            "nested_map": {"a": {"b": 2}},
            "path": ("a",),
            "expected": {"b": 2}
        },
        {
            "name": "nested_map",
            "nested_map": {"a": {"b": 2}},
            "path": ("a", "b"),
            "expected": 2
        }
    ]

    @parameterized.expand(test_cases)
    def test_access_nested_map(self, name, nested_map, path, expected):
        """test_access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
