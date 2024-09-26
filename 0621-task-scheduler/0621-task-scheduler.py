class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        freq = Counter(tasks)

        # Step 2: Create a max heap based on the task frequencies
        tasks = [-count for count in freq.values()]
        heapify(tasks)

        # Step 3: Create a deque to handle the cooldown period for tasks
        # Each entry will hold two values: [-task_count, time_task_can_be_scheduled_next]
        cooldown = deque()
        
        time = 0
        
        # Step 4: Process tasks from the heap and handle cooldowns
        while tasks or cooldown:  # Continue until no more tasks or cooldowns exist
            time += 1
            # If there are tasks in the heap, pop the most frequent one
            if tasks:
                count = 1 + heappop(tasks)  # Decrement the task count (remember they are stored as negative values)
                
                # If the task still has more occurrences, add it to the cooldown queue
                if count != 0:
                    cooldown.append([-count, n + time])  # The task can be scheduled again after 'n' units of time
                
            # If a task's cooldown period is over, push it back into the heap
            if cooldown and cooldown[0][1] == time:
                task = cooldown.popleft()[0]  # Get the task from the cooldown
                heappush(tasks, -task)  # Push the task back into the heap

        # Step 5: Return the total time taken to execute all tasks
        return time