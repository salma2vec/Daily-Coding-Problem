class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return (1 << 32) % gcd(targetX, targetY) == 0