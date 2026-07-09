class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # stored the connected component of each node
        component = [0] * n

        componentId = 0

        # built the connected components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                componentId += 1
            component[i] = componentId

        answer = []

        # answered each query
        for u, v in queries:
            answer.append(component[u] == component[v])

        return answer