func firstMissingPositive(
    nums []int,
) int {

    n := len(nums)

    // placed each valid number into its correct index.
    for i := 0; i < n; i++ {

        for nums[i] > 0 &&
            nums[i] <= n &&
            nums[i] != nums[nums[i]-1] {

            nums[i],
                nums[nums[i]-1] =
                nums[nums[i]-1],
                nums[i]
        }
    }

    // found first missing positive.
    for i := 0; i < n; i++ {

        if nums[i] != i+1 {

            return i + 1
        }
    }

    // all numbers 1..n exist.
    return n + 1
}