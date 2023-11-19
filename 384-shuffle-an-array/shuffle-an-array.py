import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.original=nums.copy()
        self.n=len(nums)

    def shuffle_list(self,lst):
        
        #Fisher-Yates shuffle algorithm
        for i in range(self.n - 1, 0, -1):
            j = random.randint(0, i)
            lst[i], lst[j] = lst[j], lst[i]    
          
        

    def reset(self) -> List[int]:
        return self.original
        
    def shuffle(self) -> List[int]:
        self.shuffle_list(self.nums)
        return self.nums

        

