class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Put all numbers into a set for O(1) lookups
        num_set = set(nums)

        # Store the longest sequence length found
        longest = 0

        # Go through each number
        for num in num_set:

            # Check if this number is the START of a sequence
            # If num - 1 exists, then this is not the start
            if num - 1 not in num_set:

                # Start counting the sequence
                length = 1

                # Current number in the sequence
                current = num

                # Keep checking next consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # Update longest sequence found
                longest = max(longest, length)

        return longest