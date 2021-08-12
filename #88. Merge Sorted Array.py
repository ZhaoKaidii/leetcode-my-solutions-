class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums2)):
            nums1[len(nums1)-i-1]=nums2[i]
        nums1.sort()
        return nums1
