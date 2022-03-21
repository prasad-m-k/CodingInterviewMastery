"""
Title: Arrays and Strings

This file contains the template for the Arrays and Strings exercises in
the DS & Algos Primer. Fill in the exercises here and refer to
arrays_and_strings_solutions.py for the complete code samples.

Execution: python arrays_and_strings.py


*** IMPORTANT NOTE ***
Python provides a lot of inbuilt functions to accomplish certain tasks. If you
are aware of these, that's great.

HOWEVER, the goal of these exercises is to understand these data structures.
Therefore, you are discouraged from writing one- to two-line functions. Instead
you will learn a lot more by implementing these things manually.

In your interview, you may want to use these inbuilt functions, but while
learning, you will learn more by doing things the hard way.
"""

"""
Exercise 1.1: Write a function that takes an integer array and reverses
the values in place

Time Complexity:
Space Complexity:
"""
def reverse_array(arr: List[int]):
    # INSERT YOUR SOLUTION HERE

"""
Exercise 1.2: Write a function that takes in a string and removes every
even-indexed character

Time Complexity:
Space Complexity:
"""
def remove_even(s: str) -> str:
    # INSERT YOUR SOLUTION HERE

"""
Exercises 1.3: Zig Zag Conversion
Full Problem Definition: https://leetcode.com/problems/zigzag-conversion/

Time Complexity:
Space Complexity:
"""
def zig_zag(s: str, num_rows: int) -> str:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 1.4: Given a 2D matrix, write a function to print the values
going back and forth across each row

Time Complexity: O(arr.length * arr[0].length)
Space Complexity: O(1)
"""
def print_back_and_forth(arr: List[List[int]]):
    # INSERT YOUR SOLUTION HERE
    
"""
Exercise 1.5: Given a 2D matrix, write a function to print the values in
the matrix in a clockwise spiral from outside to inside

Time Complexity:
Space Complexity:
"""
def print_spiral(arr: List[List[int]]):
    # INSERT YOUR SOLUTION HERE

"""
Exercise 1.6: Given a 2D matrix, write a function to print the values in the
matrix in a zig-zag order

Time Complexity:
Space Complexity:
"""
def print_diagonals(arr: List[List[int]]):
    # INSERT YOUR SOLUTION HERE

"""
Exercise 2.1: Given a string, print out all of the substrings

Time Complexity:
Space Complexity:
"""
def print_substrings(s: str):
    # INSERT YOUR SOLUTION HERE

"""
Exercise 2.2: Write a function to find all duplicates in an array. The array
will contain exactly 1 duplicated value

Time Complexity:
Space Complexity:
"""
def find_duplicates(arr: List[int]) -> int:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 2.3: Given a sorted array, find every pair of values in the
array that sum up to a given target

Time Complexity:
Space Complexity:
"""
def two_sum(arr: List[int], target: int) -> List[List[int]]:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 3.1: Given two arrays, compare them to see if they are equal

Time Complexity:
Space Complexity:
"""
def arrays_are_equal(arr1: List[int], arr2: List[int]) -> bool:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 3.2: Given two strings, determine if one string is the reverse of the
other string

Time Complexity:
Space Complexity:
"""
def strings_are_opposite(s1: str, s2: str) -> bool:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 3.3: Given two strings, determine whether they are anagrams of
each other

Time Complexity:
Space Complexity:
"""
def are_anagrams(s1: str, s2: str) -> bool:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 4.1: Given an array, compute the sum of each length-k subarray

Time Complexity:
Space Complexity:
"""
def subarray_sums(arr: List[int], k: int) -> List[int]:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 4.2: Given a string, find the longest substring of the string that does
not contain any repeated characters

Time Complexity:
Space Complexity:
"""
def no_repeated_chars(s: str) -> int:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 4.3: Given two strings, s and p, find all occurrences of anagrams of p
in s. The output is the starting index of each anagram

Time Complexity:
Space Complexity:
"""
def find_all_anagrams(s: str, p: str) -> List[int]:
    # INSERT YOUR SOLUTION HERE

"""
Exercise 4.4: Given two strings, s and p, find the smallest substring of s that
contains all the characters in p

Time Complexity:
Space Complexity:
"""
def smallest_substring(s: str, p: str) -> str:
    # INSERT YOUR SOLUTION HERE



# Sample test cases
if __name__ == '__main__':
    # INSERT YOUR TESTS HERE
