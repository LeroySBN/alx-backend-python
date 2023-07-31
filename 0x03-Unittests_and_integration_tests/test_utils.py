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

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map function.
        Checks that the correct value is returned given a specific path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test_access_nested_map_exception function.
        Checks that a KeyError is raised properly
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test_get_json function.
        Checks that utils.get_json returns the expected result."""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """TestMemoize class
    """

    def test_memoize(self):
        """test_memoize function.
        Tests that when calling a_property twice, the correct result is
        returned but a_method is only called once using assert_called_once
        """

        class TestClass:
            def a_method(self):
                """a_method function.
                """
                return 42

            @memoize
            def a_property(self):
                """a_property function.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
