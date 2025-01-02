class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = [], []

        for char in s:
            map1.append(s.index(char))  # .index() method always stores the first occurrence of the each char in s and t

        for char in t:
            map2.append(t.index(char))

        if map1 == map2:
            return True

        return False