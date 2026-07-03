var topKFrequent = function(nums, k) {
    const count = {}; // frequency of each number
    for (let num of nums) count[num] = (count[num] || 0) + 1;

    // sort keys by frequency descending and take top k
    return Object.keys(count)
        .sort((a, b) => count[b] - count[a])
        .slice(0, k)
        .map(Number);
};