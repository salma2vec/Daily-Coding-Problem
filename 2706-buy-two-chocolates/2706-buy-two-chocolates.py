class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        p=sorted(prices)
        return (money-p[0]-p[1] if p[0]+p[1]<=money else money)        