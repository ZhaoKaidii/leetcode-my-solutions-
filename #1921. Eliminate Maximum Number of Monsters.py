class Solution(object):
    def eliminateMaximum(self, dist, speed):
        n=len(dist)
        time=[(dist[i]-1)//speed[i] for i in range(n)]
        time.sort()
        for i in range(n):
            if time[i]<i:
                return i
        return n
