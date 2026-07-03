class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Used a stack to store valid scores
        record = []

        # Looped through each operation
        for op in operations:

            if op == "+":
                # Added the previous two scores
                record.append(record[-1] + record[-2])

            elif op == "D":
                # Doubled the previous score
                record.append(2 * record[-1])

            elif op == "C":
                # Removed the last score
                record.pop()

            else:
                # Added the normal integer score
                record.append(int(op))

        # Returned the final total
        return sum(record)