class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ha = defaultdict(int)
        for i in nums:
            if ha[i] > 0:
                return i
            else:
                ha[i] += 1
        