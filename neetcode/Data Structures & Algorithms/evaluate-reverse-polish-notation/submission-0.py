class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            # If the token is an operator
            if token in {"+", "-", "*", "/"}:

                # Pop the two operands
                b = stack.pop()
                a = stack.pop()

                # Perform the operation
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # Division must truncate toward zero
                    stack.append(int(a / b))

            else:
                # Push numbers onto the stack
                stack.append(int(token))

        # Final answer
        return stack[-1]