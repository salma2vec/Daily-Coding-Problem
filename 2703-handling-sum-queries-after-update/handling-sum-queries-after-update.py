class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n1 = int(''.join([str(d) for d in nums1]), 2)
        res = []
        key = False

        sum1, sum2 = n1.bit_count(), sum(nums2)
        for t, left, right in queries:
            if t == 1:
                temp = '1'*(right - left + 1) + '0'*(len(nums1) - right - 1)
                n1 ^= int(temp, 2)
                key = True
            if t == 2:
                if key:
                    sum1 = n1.bit_count()
                    key = False

                sum2 += left*sum1      
            if t == 3:
                res.append(sum2)
        
        return res                       