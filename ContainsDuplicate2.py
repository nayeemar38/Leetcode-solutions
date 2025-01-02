class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create hset for storing previous of k elements
        hset = {}
        # Traverse for all elements of the given array in a for loop
        for i in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true
            if nums[i] in hset and abs(i - hset[nums[i]]) <= k:
                return True
            hset[nums[i]] = i
        # If no duplicate element is found then return false
        return False