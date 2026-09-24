class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        # used three lists for partitioning.
        less = []
        equal = []
        greater = []

        # processed all numbers.
        for num in nums:

            if num < pivot:
                less.append(num)

            elif num > pivot:
                greater.append(num)

            else:
                equal.append(num)

        # returned the partitioned array.
        return less + equal + greater