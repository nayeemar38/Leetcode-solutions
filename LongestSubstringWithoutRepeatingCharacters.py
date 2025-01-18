#Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charSet = set()
        low = 0

        for index, val in enumerate(s):

            while val in charSet:
                charSet.remove(s[low])
                low += 1
            charSet.add(val)
            maxLength = max(maxLength, index - low + 1)

        return maxLength