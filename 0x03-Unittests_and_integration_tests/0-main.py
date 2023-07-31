#!/usr/bin/python3
"""Task 0"""

access_nested_map = __import__('utils').access_nested_map

nested_map = {"a": {"b": {"c": 1}}}
print(access_nested_map(nested_map, ["a", "b", "c"]))

print("------")
print("------")

print(access_nested_map(nested_map={"a": 1}, path=("a",)))

print("------")
print("------")

print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a",)))

print("------")
print("------")

print(access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")))
