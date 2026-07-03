class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # Used sets to track seen numbers
        seenA = set()
        seenB = set()

        # Stored the final prefix common counts
        result = []

        # Looped through both arrays
        for i in range(len(A)):

            # Added current numbers into both sets
            seenA.add(A[i])
            seenB.add(B[i])

            # Counted how many numbers are common in both sets
            common = len(seenA & seenB)

            # Added the count into the result array
            result.append(common)

        # Returned the prefix common array
        return result