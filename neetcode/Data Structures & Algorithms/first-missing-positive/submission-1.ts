class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    firstMissingPositive(nums: number[]): number {

        const n = nums.length;

        // Placed each valid number into its correct index.
        for (let i = 0; i < n; i++) {

            while (
                nums[i] > 0 &&
                nums[i] <= n &&
                nums[i] !== nums[nums[i] - 1]
            ) {

                const correctIndex =
                    nums[i] - 1;

                [
                    nums[i],
                    nums[correctIndex]
                ] = [
                    nums[correctIndex],
                    nums[i]
                ];
            }
        }

        // Found first missing positive.
        for (let i = 0; i < n; i++) {

            if (nums[i] !== i + 1) {

                return i + 1;
            }
        }

        // All numbers 1..n exist.
        return n + 1;
    }
}