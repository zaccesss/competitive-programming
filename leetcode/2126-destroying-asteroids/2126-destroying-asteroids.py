class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        # Sorted asteroids from smallest to largest.
        asteroids.sort()

        # Looped through all asteroids.
        for asteroid in asteroids:

            # Returned false if asteroid could not be destroyed.
            if mass < asteroid:
                return False

            # Added asteroid mass to planet mass.
            mass += asteroid

        # Returned true if all asteroids were destroyed.
        return True