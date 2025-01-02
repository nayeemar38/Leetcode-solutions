from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = Counter(s), Counter(t)

        if map1 == map2:
            return True
        return False