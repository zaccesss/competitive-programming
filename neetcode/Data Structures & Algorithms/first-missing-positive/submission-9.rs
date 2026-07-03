impl Solution {
    pub fn first_missing_positive(
        nums: Vec<i32>
    ) -> i32 {

        let mut nums = nums;

        let n = nums.len();

        // Placed each valid number into its correct index.
        for i in 0..n {

            while nums[i] > 0
                && nums[i] as usize <= n
                && nums[i]
                    != nums[
                        nums[i] as usize - 1
                    ]
            {

                let j =
                    nums[i] as usize - 1;

                nums.swap(i, j);
            }
        }

        // Found first missing positive.
        for i in 0..n {

            if nums[i] != (i + 1) as i32 {

                return (i + 1) as i32;
            }
        }

        // All numbers 1..n exist.
        (n + 1) as i32
    }
}