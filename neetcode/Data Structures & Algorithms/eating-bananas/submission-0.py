class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # searched for the minimum valid eating speed
        left = 1
        right = max(piles)

        while left < right:

            speed = (left + right) // 2

            # calculated the hours needed at this speed
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed

            # tried a smaller speed
            if hours <= h:
                right = speed

            # needed a larger speed
            else:
                left = speed + 1

        # returned the minimum valid speed
        return left