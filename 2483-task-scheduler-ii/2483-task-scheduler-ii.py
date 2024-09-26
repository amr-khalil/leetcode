class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        runned_tasks = {}
        time = 0

        for task in tasks:
            time += 1
            # If the task was previously runned, calculate the cooldown period
            if task in runned_tasks:
                next_available_time = runned_tasks[task] + space + 1
                time = max(time, next_available_time)
            runned_tasks[task] = time
        
        return time