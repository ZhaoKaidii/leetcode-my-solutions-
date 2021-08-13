class Solution:
    def reverseWords(self, s: str) -> str:
        s=" "+s
        word=""
        tab=""
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                word=word+s[i]
            else:
                tab=" "+word+tab
                word=""
        return tab[1:]
