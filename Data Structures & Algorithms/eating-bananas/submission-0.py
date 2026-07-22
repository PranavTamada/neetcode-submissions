class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = max(piles)
        while l <= r:
            m = (l+r)//2
            time = 0
            for i in piles:
                time += math.ceil(i/m)
            if time > h:
                l = m+1
            else:
                r = m-1
                minK = min(m,minK)
        return minK     