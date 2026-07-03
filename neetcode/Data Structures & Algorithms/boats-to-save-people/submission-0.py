class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Sort people by weight
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        # Continue until everyone has been assigned a boat
        while left <= right:

            # If the lightest and heaviest can share a boat
            if people[left] + people[right] <= limit:
                left += 1

            # The heaviest person always boards the current boat
            right -= 1

            # One boat has been used
            boats += 1

        return boats