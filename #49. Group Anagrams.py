class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        j=collections.defaultdict(list)
        for s in strs:
            k="".join(sorted(s))
            j[k].append(s)
        return list(j.values())
