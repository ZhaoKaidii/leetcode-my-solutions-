class Solution(object):
    def scoreOfParentheses(self, s):
        ans,depth,n = 0,0,len(s)
        for i in range(n):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    ans += 1 << depth
        return ans
        #bal代表了深度,假如前一个不是“（”,  即出现“））”的情况,则不需要向ans上叠加
