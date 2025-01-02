class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)  # store all nums in a hash set

        count = 0  # initially the count is 0

        for num in hash_set:  # traverse through the hash set
            if (num - 1) not in hash_set:  # if there is no prev consec num in hash_set
                length = 1  # start counting longest consec sequence from here
                while (num + length) in hash_set:  # while there are consec nums for the above num count the seq
                    length += 1
                count = max(count, length)  # only consider the max value in the entire hash_set

        return count 