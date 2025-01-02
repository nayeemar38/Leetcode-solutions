from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map1, map2 = Counter(ransomNote), Counter(magazine)

        if map1 & map2 == map1:# here the & operator performs intersection i.e min of two counters map1 and map2
        #instead of bitwise AND so the minimum of two counters should be equal to the 1st map
            return True
        return False