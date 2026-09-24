class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            # if the token is an operator
            if token in {"+", "-", "*", "/"}:

                # pop the two operands
                b = stack.pop()
                a = stack.pop()

                # perform the operation
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # division must truncate toward zero
                    stack.append(int(a / b))

            else:
                # push numbers onto the stack
                stack.append(int(token))

        # final answer
        return stack[-1]