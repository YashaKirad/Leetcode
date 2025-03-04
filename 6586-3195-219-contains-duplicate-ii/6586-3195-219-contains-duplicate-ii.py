class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ins={}

        for i,num in enumerate(nums):
            if num in ins:
                if ((abs(ins[num]-i)<=k)):
                    return True

            ins[num]=i
        return False
        