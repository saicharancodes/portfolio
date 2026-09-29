# Problem Statement
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Additional information
# 1 <= s.length <= 2 * 10^5
# The string consists of printable ASCII characters.
# You must ignore spaces, symbols, and punctuation.

# Input: "madam"  
# Output: Palindrome  

# Input: "hello"  
# Output: Not a Palindrome


# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]',"", s).lower()
        return s==s[::-1]