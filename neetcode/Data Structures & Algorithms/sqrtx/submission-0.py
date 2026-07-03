class Solution:
    def mySqrt(self, x: int) -> int:

        # Used binary search to find the square root
        left = 0
        right = x

        # Looped while the search range is valid
        while left <= right:

            # Calculated the middle number
            mid = (left + right) // 2

            # Calculated the square of mid
            square = mid * mid

            # Returned the result if a perfect square was found
            if square == x:
                return mid

            # Searched the right half if square is smaller
            elif square < x:
                left = mid + 1

            # Otherwise searched the left half
            else:
                right = mid - 1

        # Returned the rounded down square root
        return right