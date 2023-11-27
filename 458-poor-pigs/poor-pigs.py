class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = log(buckets, minutesToTest // minutesToDie + 1)
        return round(pigs) if isclose(pigs, round(pigs)) else ceil(pigs)        