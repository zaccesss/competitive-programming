class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>(); // stores frequency
        int n = nums.length;
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1); // increment count
            if (count.get(num) > n / 2) return num; // majority found
        }
        return -1;
    }
}