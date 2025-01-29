class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_count=0
        o_count=0
        t_count=0

        n=len(nums)
        for num in nums:
            if num==0:
                z_count+=1
            elif num==1:
                o_count+=1
            else:
                t_count+=1

        for i in range (z_count):
            nums[i]=0
        for i in range (z_count, o_count+z_count):
            nums[i]=1
        for i in range (o_count+z_count, n):
            nums[i]=2