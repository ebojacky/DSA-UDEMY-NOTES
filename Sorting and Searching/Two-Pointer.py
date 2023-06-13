"""The Two Pointer technique is a common algorithmic approach used in solving a variety of problems
in computer science, particularly in array and string-related questions. The technique involves using two pointers,
usually initialized at opposite ends of an array, to iterate through the array and manipulate elements.

Here is an example of how to use the Two Pointer technique to solve a problem:

Problem: Given a sorted array of integers, find if there exists a pair of elements in the array
whose sum is equal to a given target.

Example:

arr = [-2, 0, 3, 6, 8, 11]
target = 6
Solution:

We can use the Two Pointer technique to solve this problem by initializing two pointers,
one at the beginning and the other at the end of the array. We can then move the pointers towards
each other while checking if the sum of the two elements at the current positions is equal to the target.

Here's how the code would look like in Python:
"""

def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return False

#Let's test the function with the example inputs:


arr = [-2, 0, 3, 6, 8, 11]
target = 6

print(find_pair(arr, target)) # True

"""
The function returns True, indicating that there exists a pair of elements in the array whose sum is equal to the target.

Here's another example of how to use the Two Pointer technique to solve a problem:

Problem: Given a string, find the length of the longest substring without repeating characters.

Example:

s = "abcabcbb"
Solution:

We can use the Two Pointer technique to solve this problem by initializing two pointers, left and right, 
at the beginning of the string. We can then move the right pointer to the right until we encounter a 
repeating character. Once we find a repeating character, we move the left pointer to the right until we 
remove the repeating character from the substring. We continue this process until we reach the end of the string.

Here's how the code would look like in Python:

"""

def longest_substring(s):
    left = 0
    right = 0
    max_len = 0
    char_set = set()

    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
            max_len = max(max_len, len(char_set))

        else:
            char_set.remove(s[left])
            left += 1

    return max_len

#Let's test the function with the example input:

s = "abcabcbb"

print(longest_substring(s)) # 3

#The function returns 3, indicating that the longest substring without repeating characters is "abc"."""