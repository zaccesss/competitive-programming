class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # sort people by weight
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        # continue until everyone has been assigned a boat
        while left <= right:

            # if the lightest and heaviest can share a boat
            if people[left] + people[right] <= limit:
                left += 1

            # the heaviest person always boards the current boat
            right -= 1

            # one boat has been used
            boats += 1

        return boats