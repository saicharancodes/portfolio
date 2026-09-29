class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count[s[i], 0]
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        return s_count == t_count


#for multiple anagram

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = defalutdict(list)

        for w in strs:
            s = ''.join(sorted(w))
            a[s].append(w)
        return list(a.values())
