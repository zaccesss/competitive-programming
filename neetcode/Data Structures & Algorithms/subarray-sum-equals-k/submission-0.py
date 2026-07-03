class Solution:
    def subarraySum(self, nums, k):

        prefix_count = {0: 1}  # prefix sum frequency map
        current_sum = 0        # running sum
        count = 0              # total valid subarrays

        for num in nums:

            current_sum += num  # update running sum

            # check if a previous prefix sum can form sum k
            if current_sum - k in prefix_count:
                count += prefix_count[current_sum - k]

            # store/update current prefix sum count
            prefix_count[current_sum] = (
                prefix_count.get(current_sum, 0) + 1
            )

        return count