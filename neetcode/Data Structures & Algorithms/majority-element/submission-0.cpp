class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> count; // stores frequency of each number
        int n = nums.size();
        for (int num : nums) {
            count[num]++; // increment count for this number
            if (count[num] > n / 2) return num; // if it exceeds n/2, it's the majority
        }
        return -1;
    }
};