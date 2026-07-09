class Solution:
    def simplifyPath(self, path: str) -> str:

        # stored the directories in the simplified path
        stack = []

        # processed each part of the path
        for part in path.split("/"):

            # ignored empty parts and current directory
            if part == "" or part == ".":
                continue

            # moved to the parent directory
            if part == "..":
                if stack:
                    stack.pop()

            # added a valid directory
            else:
                stack.append(part)

        # returned the simplified path
        return "/" + "/".join(stack)