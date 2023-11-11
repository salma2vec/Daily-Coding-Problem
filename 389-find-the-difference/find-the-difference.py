class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        added_letter = (counter_t - counter_s).popitem()[0]

        return added_letter


sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))  # Output: "e"
print(sol.findTheDifference("", "y"))  # Output: "y"
        