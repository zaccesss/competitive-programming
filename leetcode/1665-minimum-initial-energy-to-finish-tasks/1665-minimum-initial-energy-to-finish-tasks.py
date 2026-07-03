class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # Sort tasks by (minimum - actual) descending
        # Tasks needing the biggest extra energy go first
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        # Current energy
        energy = 0

        # Minimum initial energy needed
        answer = 0

        for actual, minimum in tasks:

            # If current energy is less than required minimum
            if energy < minimum:

                # Increase initial energy needed
                answer += minimum - energy

                # Update current energy
                energy = minimum

            # Complete the task
            energy -= actual

        return answer