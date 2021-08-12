class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def takefirst(ele):
            return ele[0]
        s=collections.Counter(words)
        d=[[s[i],i] for i in s]
        d.sort()
        d.sort(key=takefirst,reverse=True)
        p=[i[1] for  i in d]
        return p[0:k]
