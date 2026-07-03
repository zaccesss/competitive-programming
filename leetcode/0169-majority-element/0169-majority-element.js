var majorityElement = function(nums) {
    const count = {}; // stores frequency of each number
    const n = nums.length;
    for (let num of nums) {
        count[num] = (count[num] || 0) + 1; // increment count
        if (count[num] > n / 2) return num; // majority found
    }
};