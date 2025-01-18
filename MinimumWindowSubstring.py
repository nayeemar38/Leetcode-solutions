#Sliding Window
from collections import Counter
class Solution:
    def minWindow(self, s, t) -> str:
        if not t or not s:
            return ""

        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)

        # Sliding window pointers
        l, r = 0, 0

        # Formed keeps track of how many characters meet the frequency in t
        formed = 0
        window_count = {}

        # Result: (window_length, left, right)
        res = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            # If the current character's frequency matches t's
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Try to shrink the window
            while l <= r and formed == required:
                char = s[l]

                # Update the result
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)

                # Remove the leftmost character
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1

                l += 1

            # Expand the window
            r += 1

        # Return the smallest window or an empty string if no valid window exists
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]