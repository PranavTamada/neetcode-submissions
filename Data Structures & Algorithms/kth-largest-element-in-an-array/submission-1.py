class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ints = []
        for num in nums:
            heapq.heappush(ints,-num)
        for i in range(k):
            ret = heapq.heappop(ints)
        return -ret