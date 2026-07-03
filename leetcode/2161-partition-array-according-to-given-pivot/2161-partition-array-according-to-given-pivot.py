class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        # Used three lists for partitioning.
        less = []
        equal = []
        greater = []

        # Processed all numbers.
        for num in nums:

            if num < pivot:
                less.append(num)

            elif num > pivot:
                greater.append(num)

            else:
                equal.append(num)

        # Returned the partitioned array.
        return less + equal + greater