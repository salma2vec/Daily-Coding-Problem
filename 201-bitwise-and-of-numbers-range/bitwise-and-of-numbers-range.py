class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = bin(left)[2:], bin(right)[2:]
        if len(left) != len(right):
            return 0
        ans = ''
        for i in range(len(left)):
            if left[i] == right[i]:
                ans += left[i]
            else:
                break
        ans += '0' * (len(left)-len(ans))
        return int(ans, 2)
              