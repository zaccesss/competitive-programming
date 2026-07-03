class Solution {
    func firstMissingPositive(
        _ nums: inout [Int]
    ) -> Int {

        let n = nums.count

        // Placed each valid number into its correct index.
        for i in 0..<n {

            while
                nums[i] > 0 &&
                nums[i] <= n &&
                nums[i] != nums[nums[i] - 1]
            {

                let temp = nums[i]

                nums[i] =
                    nums[temp - 1]

                nums[temp - 1] =
                    temp
            }
        }

        // Found first missing positive.
        for i in 0..<n {

            if nums[i] != i + 1 {

                return i + 1
            }
        }

        // All numbers 1..n exist.
        return n + 1
    }
}