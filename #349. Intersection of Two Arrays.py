class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1,nums2,s=set(nums1),set(nums2),[]
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    s.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    s.append(i)
        return s
