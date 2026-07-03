 class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {

        int n = nums.size();

        // Placed each valid number into its correct index.
        for (int i = 0; i < n; i++) {

            while (
                nums[i] > 0 &&
                nums[i] <= n &&
                nums[i] != nums[nums[i] - 1]
            ) {

                swap(
                    nums[i],
                    nums[nums[i] - 1]
                );
            }
        }

        // Found first missing positive.
        for (int i = 0; i < n; i++) {

            if (nums[i] != i + 1) {

                return i + 1;
            }
        }

        // All numbers 1..n exist.
        return n + 1;
    }
};