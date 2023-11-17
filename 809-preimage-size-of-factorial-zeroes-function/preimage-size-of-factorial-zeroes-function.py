class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_trailing_zeros(n: int) -> int:
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        def atMost_k(k: int) -> int:
            left, right = 0, 5 * k + 4

            while left <= right:
                mid = (left + right) // 2
                count = count_trailing_zeros(mid)

                if count <= k:
                    left = mid + 1
                else:
                    right = mid - 1

            return right

        return atMost_k(k) - atMost_k(k - 1)   