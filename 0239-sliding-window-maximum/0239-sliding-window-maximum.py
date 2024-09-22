class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use deque (double-ended queue)
        n = len(nums)
        ans = []
        deq = collections.deque()
        
        # fill the deque
        for r in range(k):
            # Remove elements from deque if they are smaller than the current element
            while deq and nums[r] >= nums[deq[-1]]:
                deq.pop()
            deq.append(r)
        
        # Add the maximum of the first window to the answer list
        ans.append(nums[deq[0]])
        
        # Process the rest of the windows
        for r in range(k, n):
            # Remove elements that are out of the current window
            if deq and deq[0] == r - k:
                deq.popleft()
            
            # Maintain the decreasing order in deque
            while deq and nums[r] >= nums[deq[-1]]:
                deq.pop()
            deq.append(r)
            
            # Append the current maximum (front of deque) to the answer list
            ans.append(nums[deq[0]])

        return ans