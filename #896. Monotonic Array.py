class Solution(object):   
    def isMonotonic(self, A):
        p=[c for c in A]
        if len(A)<3:
                    return True
        else:
            A.sort(reverse=False)
            s1=(A==p)
            A.sort(reverse=True)
            s2=(A==p)
        return s1 or s2
