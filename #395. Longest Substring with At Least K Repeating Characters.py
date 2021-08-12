class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        for c in set(s):
            if s.count(c)<k:
                return max(self.longestSubstring(st,k) for st in s.split(c))
        return len(s)
