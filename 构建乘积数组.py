class Solution(object):
    def constructArr(self, a):
        B,t=[1]*len(a),1
        for i in range(1,len(a)):
            B[i]=B[i-1]*a[i-1]
        for i in range(len(a)-2,-1,-1):
            t=t*a[i+1]
            B[i]=B[i]*t           
        return B
