class Solution:
    def decodeString(self, s: str) -> str:

        # stored the previous strings and repeat counts
        stack = []

        # built the current repeat count
        number = 0

        # built the current decoded string
        current = ""

        # processed each character
        for ch in s:

            # built a multi-digit number
            if ch.isdigit():
                number = number * 10 + int(ch)

            # started a new encoded substring
            elif ch == "[":
                stack.append((current, number))
                current = ""
                number = 0

            # finished an encoded substring
            elif ch == "]":
                previous, repeat = stack.pop()
                current = previous + current * repeat

            # added a normal character
            else:
                current += ch

        # returned the decoded string
        return current