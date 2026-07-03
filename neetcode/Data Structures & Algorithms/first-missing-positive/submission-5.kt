class Solution {
    fun firstMissingPositive(nums: IntArray): Int {

        val n = nums.size

        // Placed each valid number into its correct index.
        for (i in 0 until n) {

            while (
                nums[i] > 0 &&
                nums[i] <= n &&
                nums[i] != nums[nums[i] - 1]
            ) {

                val temp = nums[i]

                nums[i] =
                    nums[temp - 1]

                nums[temp - 1] =
                    temp
            }
        }

        // Found first missing positive.
        for (i in 0 until n) {

            if (nums[i] != i + 1) {

                return i + 1
            }
        }

        // All numbers 1..n exist.
        return n + 1
    }
}