class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            # I assumed the current asteroid survives until a collision destroys it.
            alive = True

            # I kept checking while a collision was possible.
            while alive and asteroid < 0 and stack and stack[-1] > 0:

                # The asteroid on the stack was smaller, so it exploded.
                if stack[-1] < -asteroid:
                    stack.pop()

                # Both asteroids were the same size, so both exploded.
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False

                # The asteroid on the stack was larger, so the current asteroid exploded.
                else:
                    alive = False

            # I added the current asteroid if it survived all collisions.
            if alive:
                stack.append(asteroid)

        return stack