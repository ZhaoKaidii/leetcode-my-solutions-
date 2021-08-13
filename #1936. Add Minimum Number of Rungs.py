class Solution(object):
    def addRungs(self, rungs, dist):
        c=0
        if len(rungs)==1:
            return (rungs[0]//dist-1) if (rungs[0])%dist==0 else (rungs[0])//dist
        rungs=[0]+rungs
        for i in range(len(rungs)-1):
            if (rungs[i+1]-rungs[i])>dist:
                d=((rungs[i+1]-rungs[i])//dist-1) if (rungs[i+1]-rungs[i])%dist==0 else (rungs[i+1]-rungs[i])//dist
                c+=d
        return c
