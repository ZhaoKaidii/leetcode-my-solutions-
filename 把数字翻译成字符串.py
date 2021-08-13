class Solution:
    def translateNum(self, num: int) -> int:
        s=str(num)
        if len(s)<2:
            return len(s)
        if len(s)==2:
            return 1+int(s<="25")
        dp=[0]*len(s)
        dp[0],dp[1]=1,1+int(s[0:2]<="25")
        for  i in range(2,len(s)):
            dp[i]=dp[i-1]+int("10"<=(s[i-1]+s[i])<="25")*dp[i-2]
        return dp[-1]
