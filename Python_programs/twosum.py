# Two Sum
# CloudflareCloudflare
# Easy
# Programming
# Arrays
# Hash Tables
# DSA
# Problem Statement
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Additional information
# The array will contain at least 2 elements.
# Only one valid answer exists.
# The function should return the indices, not the values.

# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9

# Output: [0, 1]
# Example 2:

# Input: nums = [3, 2, 4], target = 6

# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6

# Output: [0, 1]

#answer

nums = [2, 7, 11, 15], target = 9

l = {}

for i , num in enumerate(nums):
    req = target - num

    if req in l:
        print(l[req], i)
    l[num]=i