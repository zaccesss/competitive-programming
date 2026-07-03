class Solution:
    def minJumps(self, nums: List[int]) -> int:

        from collections import defaultdict, deque

        n = len(nums)

        if n == 1:  # already at the end
            return 0

        MAX = max(nums)

        spf = list(range(MAX + 1))  # smallest prime factor sieve

        for i in range(2, int(MAX ** 0.5) + 1):

            if spf[i] == i:  # i is prime

                for j in range(i * i, MAX + 1, i):

                    if spf[j] == j:
                        spf[j] = i

        divisible = defaultdict(list)  # prime -> divisible indices

        for i, num in enumerate(nums):

            used = set()  # avoid duplicate factors

            while num > 1:

                p = spf[num]  # get prime factor fast

                if p not in used:
                    divisible[p].append(i)
                    used.add(p)

                while num % p == 0:  # remove repeated factor
                    num //= p

        q = deque([0])  # BFS starts at index 0

        vis = [0] * n  # visited array
        vis[0] = 1

        usedPrime = set()  # avoid reprocessing teleport

        jumps = 0

        while q:

            for _ in range(len(q)):  # process one BFS level

                i = q.popleft()

                if i == n - 1:  # reached end
                    return jumps

                for nxt in (i - 1, i + 1):  # adjacent moves

                    if 0 <= nxt < n and not vis[nxt]:
                        vis[nxt] = 1
                        q.append(nxt)

                x = nums[i]

                # teleport only if current value is prime
                if x > 1 and spf[x] == x and x not in usedPrime:

                    usedPrime.add(x)

                    for nxt in divisible[x]:  # jump to divisible indices

                        if not vis[nxt]:
                            vis[nxt] = 1
                            q.append(nxt)

            jumps += 1  # finished one BFS layer