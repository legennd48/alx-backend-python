#!/usr/bin/env python3
'''
This module contains unit tests for the `access_nested_map`,
`get_json`, and `memoize` functions
defined in the `utils.py` module.
'''
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function, which retrieves
    values from nested dictionaries.

    This class provides unit tests to verify that
    `access_nested_map` correctly accesses
    values within nested dictionaries based on a provided path.
    """

    @parameterized.expand([
        ("{'a': 1}", ("a",), 1),
        ("{'a': {'b': 2}}", ("a",), {'b': 2}),
        ("{'a': {'b': 2}}", ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: str,
        path: Tuple[str],
        expected: Union[Dict, int],
    ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(
            access_nested_map(nested_map, path), expected
        )

    @parameterized.expand([
        ("{}", ("a",), KeyError),
        ("{'a': 1}", ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: str,
        path: Tuple[str],
        exception: Exception
    ) -> None:
        """Tests `access_nested_map`'s exception raising.

        This test verifies that the function raises the
        appropriate exception (KeyError)
        when the requested key is not found in the nested map.
        Args:
            nested_map (str): A string representation of the nested
            dictionary to access.
            This is converted to a dictionary before testing.
            path (Tuple[str]): A tuple representing the path to
            traverse within the nested map.
            exception (Exception): The expected exception to be raised.
            description (str): A description of the current test case.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """

    This class provides unit tests to verify that `get_json`
    makes a GET request to the provided URL and returns
    the parsed JSON data.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
    ) -> None:
        """Tests `get_json`'s output.

        This test verifies that the function returns the expected
        data (payload or empty dict)
        based on the mocked response of the GET request.

        Args:
            test_url (str): The URL to fetch JSON data from.
            test_payload (Dict): The expected payload returned by the
            mocked GET request.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function, which caches the results of a fctn call.

    This class provides a unit test to verify that the
    `memoize` decorator effectively caches
    the result of a function call and avoids redundant computations.
    """

    def test_memoize(self) -> None:
        """Tests `memoize`'s output.

        This test verifies that the decorated function's
        result is cached and returned
        on subsequent calls without re-executing the original function.

        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
