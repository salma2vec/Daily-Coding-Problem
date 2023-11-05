class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow, fast = n, n
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                break
        
        return slow == 1        