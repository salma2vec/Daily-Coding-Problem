class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while n // factor > 0:
            curr = (n // factor) % 10
            after = n % factor
            before = n // (factor * 10)

            count += before * factor + (curr == 1) * (after + 1) + (curr > 1) * factor

            factor *= 10

        return count     