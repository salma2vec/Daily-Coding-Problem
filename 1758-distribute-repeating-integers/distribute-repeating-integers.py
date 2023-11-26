class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        data = list(Counter(nums).values())
        quantity.sort(reverse=True)

        k = len(data)
        m = len(quantity)

        def recursive(j):
            if j == m:
                return True
            elem = quantity[j]

            for i in range(k):
                if data[i] >= elem:
                    data[i] -= elem
                    if recursive(j + 1):
                        return True
                    data[i] += elem
            return False
        
        return recursive(0)        