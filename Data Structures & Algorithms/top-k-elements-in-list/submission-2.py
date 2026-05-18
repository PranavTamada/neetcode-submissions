class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = Counter(nums)
        maxi = max(freq.values())
        cnt = 0
        while cnt < k:
            for j in freq.keys():
                if freq[j] == maxi and cnt < k:
                    output.append(j)
                    cnt += 1
            maxi -= 1
        return output
