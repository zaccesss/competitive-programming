class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        result = []

        # pointers for each interval list
        i = 0
        j = 0

        # traverse both lists until one is exhausted
        while i < len(firstList) and j < len(secondList):

            # find the overlapping interval
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # if a valid intersection exists, add it to the result
            if start <= end:
                result.append([start, end])

            # move the pointer whose interval ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result