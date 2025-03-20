"""
981. Time Based Key-Value Store
link: https://leetcode.com/problems/time-based-key-value-store/
"""


class TimeMap:
    """
    Set(): O(1)
    Get(): O(log n)
    """

    def __init__(self):
        self.store: dict[str, list] = {}  # key: [[val, time], ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        data = self.store[key]
        answer = ""
        l, r = 0, len(data) - 1

        while l <= r:
            mid = (l + r) // 2

            # Verbose
            # ----------------------------------------------------------
            # if data[mid][1] == timestamp:
            #     answer = data[mid][0]
            #     r = mid - 1  # searching the most first appearance
            # elif data[mid][1] < timestamp:
            #     answer = data[mid][0]
            #     l = mid + 1  # Update to closer to timestamp
            # ---------------------------------------------------------

            # value is in valid range, update closer to timestamp
            if data[mid][1] <= timestamp:
                answer = data[mid][0]
                l = mid + 1

            else:  # value grate then timestamp invalid range
                r = mid - 1

        return answer
