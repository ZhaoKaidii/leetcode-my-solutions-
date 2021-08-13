class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        tt=[f for f in text.split(" ")]
        c=len(tt)
        if len(brokenLetters)==0:
            return c
        for  i in range(len(tt)):
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in tt[i]:
                    c-=1
                    break
        return c
