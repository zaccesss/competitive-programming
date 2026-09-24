class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        # sorted asteroids from smallest to largest.
        asteroids.sort()

        # looped through all asteroids.
        for asteroid in asteroids:

            # returned false if asteroid could not be destroyed.
            if mass < asteroid:
                return False

            # added asteroid mass to planet mass.
            mass += asteroid

        # returned true if all asteroids were destroyed.
        return True