import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneslist = []
        for stone in stones:
            heapq.heappush(stoneslist,-stone)
        while len(stoneslist) > 1:
            first = -heapq.heappop(stoneslist)
            second = -heapq.heappop(stoneslist)           
            diff = first-second
            if diff > 0:
                heapq.heappush(stoneslist,-diff)
        if len(stoneslist) > 0:
            return -stoneslist[0]
        else:
            return 0