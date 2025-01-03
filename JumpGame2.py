class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables
        min_jumps = 0  # Number of jumps
        max_reach = 0  # Maximum index reachable so far
        end_of_current_jump = 0  # The end of the current jump range

        # Iterate through the array except the last element
        for i in range(len(nums) - 1):
            # Update the maximum reach
            max_reach = max(max_reach, i + nums[i])

            # If we reach the end of the current jump range
            if i == end_of_current_jump:
                min_jumps += 1  # Make a jump
                end_of_current_jump = max_reach  # Set new jump range

                # If we can already reach or exceed the end, break early
                if end_of_current_jump >= len(nums) - 1:
                    break

        return min_jumps