class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        need = len(set(s1))
        for i in range(len(s2)):
            count2 = defaultdict(int)
            curr = 0
            for j in range(i,len(s2)):
                count2[s2[j]] += 1
                if count2[s2[j]] > freq1[s2[j]]:
                    break
                elif count2[s2[j]] == freq1[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
        return False
                