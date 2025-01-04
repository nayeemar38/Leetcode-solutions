class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0  # left pointer
        right = len(height) - 1  # right pointer
        left_max = height[left]
        right_max = height[right]
        water = 0  # initially the amout of water than can be stored is 0

        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])  # new left max
                water += left_max - height[left]  # add water
            else:
                right -= 1
                right_max = max(right_max, height[right])  # new right max
                water += right_max - height[right]  # add water

        return water