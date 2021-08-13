class Solution(object):
    def rotate(self, nums, k):
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n=len(nums)
        k%=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
