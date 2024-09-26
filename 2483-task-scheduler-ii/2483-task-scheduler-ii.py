class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_executed = {}
        time = 0

        for task in tasks:
            time += 1
            if task in last_executed:
                next_available_time = last_executed[task] + space + 1
                time = max(time, next_available_time)
            last_executed[task] = time
        return time