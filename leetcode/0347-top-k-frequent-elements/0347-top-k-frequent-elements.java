class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>(); // frequency map
        for (int num : nums) count.put(num, count.getOrDefault(num, 0) + 1);

        // min heap of size k, sorted by frequency
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (a, b) -> count.get(a) - count.get(b)
        );
        for (int num : count.keySet()) {
            heap.offer(num);
            if (heap.size() > k) heap.poll(); // remove least frequent
        }

        int[] result = new int[k];
        for (int i = 0; i < k; i++) result[i] = heap.poll();
        return result;
    }
}