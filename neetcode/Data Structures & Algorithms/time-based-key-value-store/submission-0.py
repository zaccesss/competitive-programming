class TimeMap:

    def __init__(self):
        # Map each key to a list of (timestamp, value)
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Create a new list if the key doesn't exist
        if key not in self.mp:
            self.mp[key] = []

        # Append the new timestamp-value pair
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Return empty string if the key doesn't exist
        if key not in self.mp:
            return ""

        arr = self.mp[key]
        l, r = 0, len(arr) - 1
        ans = ""

        # Binary search for the latest valid timestamp
        while l <= r:
            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                ans = arr[m][1]
                l = m + 1
            else:
                r = m - 1

        return ans