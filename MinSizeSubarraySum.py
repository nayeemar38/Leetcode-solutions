#Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, low = 0,0
        ans = len(nums)

        if sum(nums) < target: return 0

        for i, val in enumerate(nums):
            s += val
            while s >= target:
                s -= nums[low]
                ans = min(ans,i - low + 1)

                low+=1
        return ans