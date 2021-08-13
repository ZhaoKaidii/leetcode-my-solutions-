class Solution:
    def jump(self, nums: List[int]) -> int:
        step,mp,end=0,0,0
        for i in range(len(nums)-1):
            if mp>=i:
                mp=max(mp,nums[i]+i)
                #更新最大位置
                if i==end:
                   #当指针i指向end的时候，mp已经统计了i到end之间每个格子能到的最大位置，将end更新至mp，step加一
                    end=mp
                    step+=1
        return step
