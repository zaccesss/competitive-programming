class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # check if a ship capacity can finish within the given days
        def canShip(capacity):

            daysNeeded = 1
            currentWeight = 0

            for weight in weights:

                if currentWeight + weight > capacity:
                    daysNeeded += 1
                    currentWeight = 0

                currentWeight += weight

            return daysNeeded <= days

        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left