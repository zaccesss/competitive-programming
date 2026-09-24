class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # used sets to track seen numbers
        seenA = set()
        seenB = set()

        # stored the final prefix common counts
        result = []

        # looped through both arrays
        for i in range(len(A)):

            # added current numbers into both sets
            seenA.add(A[i])
            seenB.add(B[i])

            # counted how many numbers are common in both sets
            common = len(seenA & seenB)

            # added the count into the result array
            result.append(common)

        # returned the prefix common array
        return result