class Solution {
    public int firstMissingPositive(int[] nums) {

        int n = nums.length;

        // placed each valid number into its correct index.
        for (int i = 0; i < n; i++) {

            while (
                nums[i] > 0 &&
                nums[i] <= n &&
                nums[i] != nums[nums[i] - 1]
            ) {

                int temp = nums[i];

                nums[i] =
                    nums[temp - 1];

                nums[temp - 1] =
                    temp;
            }
        }

        // found first missing positive.
        for (int i = 0; i < n; i++) {

            if (nums[i] != i + 1) {

                return i + 1;
            }
        }

        // all numbers 1..n exist.
        return n + 1;
    }
}