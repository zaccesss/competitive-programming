class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # paired each car with its position and speed
        cars = list(zip(position, speed))

        # sorted the cars from closest to the target to farthest
        cars.sort(reverse=True)

        # stored the arrival times of each fleet
        stack = []

        for pos, spd in cars:

            # calculated the time needed to reach the target
            time = (target - pos) / spd

            # formed a new fleet if this car could not catch the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)