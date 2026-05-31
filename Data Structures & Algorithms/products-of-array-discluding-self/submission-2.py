class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        flag0 = 0
        res = []
        for i in nums:
            if i == 0:
                if not flag0 <= 1:
                    prod = 0
                flag0 += 1
            else:
                prod *= i
        for i in nums:
            if flag0 > 1:
                res.append(0)
            elif flag0 == 0:
                res.append(int(prod/i))
            else:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
        return res

        
