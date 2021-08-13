class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first)-len(second))>1:
            return False
        c=0
        if len(first)==len(second):
            i=0
            while i<len(first):

                if first[i]!=second[i]:
                    c+=1
                if c>1:
                    return False
                i+=1
        elif len(first)>len(second):
            i=j=0
            while i<len(second) and j<len(first):
                if first[j]!=second[i]:
                    c+=1
                    j+=1
                    if c>1:
                        return False
                    continue
                j+=1
                i+=1
        else:
            i=j=0
            while i<len(first) and j<len(second):
                if second[j]!=first[i]:
                    c+=1
                    j+=1
                    if c>1:
                        return False
                    continue
                j+=1
                i+=1
        return True
