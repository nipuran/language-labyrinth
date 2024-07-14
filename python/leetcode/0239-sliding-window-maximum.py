from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    l = r = 0
    output = list()
    q = deque()
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        if l > q[0]:
            q.popleft()
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output

# case 1:
nums1 = [1,3,-1,-3,5,3,6,7]
k1 = 3
case1 = maxSlidingWindow(nums1, k1)
print(case1)

# case 2:
nums2 = [1]
k2 = 1
case2 = maxSlidingWindow(nums2, k2)
print(case2)

