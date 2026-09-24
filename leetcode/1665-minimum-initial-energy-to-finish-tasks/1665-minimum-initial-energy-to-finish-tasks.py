class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # sort tasks by (minimum - actual) descending
        # tasks needing the biggest extra energy go first
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        # current energy
        energy = 0

        # minimum initial energy needed
        answer = 0

        for actual, minimum in tasks:

            # if current energy is less than required minimum
            if energy < minimum:

                # increase initial energy needed
                answer += minimum - energy

                # update current energy
                energy = minimum

            # complete the task
            energy -= actual

        return answer