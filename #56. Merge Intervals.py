class Solution(object):
    def merge(self,intervals):
        intervals.sort(key=lambda x:x[0])
        ss=[intervals[0]]
        for i in range(1,len(intervals)):
            for j in range(len(ss)):
                hh=intervals[i]
                u=(intervals[i][0]<=ss[j][1] and intervals[i][0]>=ss[j][0]) or (ss[j][0]<=intervals[i][1] and ss[j][0]>=intervals[i][0])
                if u:
                    hh=[min(hh[0],ss[j][0]),max(hh[1],ss[j][1])]
                    ss[j]=hh
                elif (not u) and j<len(ss)-1:
                    continue
                else:
                    ss.append(hh)
                    break
        return ss
