class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # used a stack to store valid scores
        record = []

        # looped through each operation
        for op in operations:

            if op == "+":
                # added the previous two scores
                record.append(record[-1] + record[-2])

            elif op == "D":
                # doubled the previous score
                record.append(2 * record[-1])

            elif op == "C":
                # removed the last score
                record.pop()

            else:
                # added the normal integer score
                record.append(int(op))

        # returned the final total
        return sum(record)