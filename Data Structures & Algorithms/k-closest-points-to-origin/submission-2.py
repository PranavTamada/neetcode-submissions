class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x,y in points:
            heapq.heappush(dist,(math.sqrt((x)**2 + (y)**2),[x,y]))
        print(dist)
        out = []
        for i in range(k):
            out.append(heapq.heappop(dist)[1])
        return out