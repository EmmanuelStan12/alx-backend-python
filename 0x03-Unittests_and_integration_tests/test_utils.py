#!/usr/bin/env python3
"""Testing the client py file
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized

from utils import (
    access_nested_map
)

class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """Tests `access_nested_map` output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str]
    ) -> None:
        """Tests `access_nested_map` throws exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
