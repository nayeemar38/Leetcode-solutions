class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        anagram_map = defaultdict(list)  # initialize a defaultdict of type list

        for word in strs:
            sorted_word = ''.join(sorted(word))  # sort every word in strs
            anagram_map[sorted_word].append(word)  # store the sorted word with its anagrams together

        return list(anagram_map.values())  # return the values of the hashmap in list format