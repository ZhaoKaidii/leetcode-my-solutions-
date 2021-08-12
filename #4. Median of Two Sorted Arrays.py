class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A=nums1+nums2
        A.sort(reverse=False)
        l=len(A)
        LL=0
        if l%2==0:
                 ll=(A[int(l/2)]+A[int(l/2)-1])/2
        else:
                 ll=A[int(l/2)]
        return ll
