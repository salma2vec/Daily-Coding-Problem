class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = defaultdict(list)
        for i, v in enumerate(nums):
            self.hashmap[v].append(i)

    def pick(self, target: int) -> int:
        indxs = self.hashmap[target]
        length = len(indxs)
        indx = randint(0, length-1)
        return indxs[indx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)