class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # put all numbers into a set for O(1) lookups
        num_set = set(nums)

        # store the longest sequence length found
        longest = 0

        # go through each number
        for num in num_set:

            # check if this number is the START of a sequence
            # if num - 1 exists, then this is not the start
            if num - 1 not in num_set:

                # start counting the sequence
                length = 1

                # current number in the sequence
                current = num

                # keep checking next consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # update longest sequence found
                longest = max(longest, length)

        return longest