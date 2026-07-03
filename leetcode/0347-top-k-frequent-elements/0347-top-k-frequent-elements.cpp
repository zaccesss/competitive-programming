class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count; // frequency of each number
        for (int num : nums) count[num]++; // count each number

        // sort numbers by frequency descending
        vector<pair<int,int>> freq(count.begin(), count.end());
        sort(freq.begin(), freq.end(), [](auto& a, auto& b){
            return a.second > b.second;
        });

        vector<int> result;
        for (int i = 0; i < k; i++) result.push_back(freq[i].first); // take top k
        return result;
    }
};