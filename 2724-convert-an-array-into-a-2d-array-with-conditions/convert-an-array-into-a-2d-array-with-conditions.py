class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        while count_map:
            temp = []
            for key, count in list(count_map.items()):
                temp.append(key)
                count_map[key] -= 1
                if count_map[key] == 0:
                    del count_map[key]
            ans.append(temp)

        return ans        