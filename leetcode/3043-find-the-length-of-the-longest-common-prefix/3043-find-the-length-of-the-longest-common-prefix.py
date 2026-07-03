class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        # Used a set to store all prefixes from arr1
        prefixes = set()

        # Looped through every number in arr1
        for num in arr1:

            num = str(num)

            # Added every possible prefix into the set
            for i in range(1, len(num) + 1):
                prefixes.add(num[:i])

        # Stored the maximum prefix length found
        longest = 0

        # Looped through every number in arr2
        for num in arr2:

            num = str(num)

            # Checked every prefix of the current number
            for i in range(1, len(num) + 1):

                # Updated the answer if the prefix exists
                if num[:i] in prefixes:
                    longest = max(longest, i)

        # Returned the longest common prefix length
        return longest