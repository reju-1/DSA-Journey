"""
621. Task Scheduler
link: https://leetcode.com/problems/task-scheduler/
"""

import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        Time: O(m), where m is the total number of tasks.
        Space: O(1), since the heap and queue store at most 26 task types.

        Approach:
            - Count the frequency of each task.
            - Use a max-heap to always schedule the task with the highest remaining frequency.
            - Use a queue to manage coolDowns; once a task has cooled down, push it back to the heap.
        """

        frequency = {}
        for t in tasks:
            frequency[t] = 1 + frequency.get(t, 0)

        maxHeap = [-f for f in frequency.values()]
        heapq.heapify(maxHeap)

        queue = deque()  # [(remaining_freq, available_time),]
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time + n))

            if queue and queue[0][1] == time:  # availableTime == currentTime
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
