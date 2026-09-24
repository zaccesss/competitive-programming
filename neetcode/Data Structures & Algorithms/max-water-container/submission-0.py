class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1

        # used answer to store maximum area.
        answer = 0

        while left < right:

            width = right - left

            height = min(
                heights[left],
                heights[right]
            )

            # calculated current container area.
            area = width * height

            answer = max(
                answer,
                area
            )

            # moved the smaller height.
            if heights[left] < heights[right]:

                left += 1

            else:

                right -= 1

        # returned maximum area.
        return answer