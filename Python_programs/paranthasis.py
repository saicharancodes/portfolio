# class Solution:

# def isValid(self, s: str) -> bool:

# stack = []

# map = {")":"(", "}":"{", "[":"]"}


# for c in s:

# if c in map.values():

# stack.append(c):

# elif c in map.keys():

# if not stack or map[c] != stack.pop():

# return False

# return not stack