class Solution(object):
    def removeDuplicateLetters(self, s):
        ss= []
        c=collections.Counter(s)
        for y in s:
                if y not in ss:
                    while len(ss)>0 and y<ss[-1] and c[ss[-1]]>0:
                        ss.pop()                                                
                        ss.append(y)
                    c[y]-=1                                                                              
        return ''.join(ss)
