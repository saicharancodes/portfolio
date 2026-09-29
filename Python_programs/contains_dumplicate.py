class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()       #hash set
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False