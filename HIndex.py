class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        for index,value in enumerate(citations):
            if len(citations) - index <= value:
                return len(citations) - index
        return 0