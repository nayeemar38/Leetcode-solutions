class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize a pointer to track position in s
        i = 0

        # Iterate over string t
        for char in t:
            # If current character in t matches the current character in s, move the pointer
            if i < len(s) and char == s[i]:
                i += 1

        # If the pointer has moved through all characters in s, return True
        return i == len(s)