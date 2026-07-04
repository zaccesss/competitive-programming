class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        result = []

        # Pointers for each intervval list
        i = 0
        j = 0

        # Transverse both lisrs until one is exhusted 
        while i < len(firstList) and j < len(secondList):

            # Find the overlapping interval
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If a valid intersection exists, add it to the result
            if start <= end:
                result.append([start, end])

            # Move the pointer whose interval ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result