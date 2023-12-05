class Solution:
    def uniqueLetterString(self, s: str) -> int:
        li = []
        for i in range(26):
            temp = []
            temp.append(-1) 
            li.append(temp)
        for i in range(len(s)):
            li[ord(s[i]) - 65].append(i)
        ans = 0
        for each in li:
            each.append(len(s))
            for i in range(1, len(each) - 1): 
                ans += ((each[i] - each[i - 1]) * (each[i + 1] - each[i]))
        return ans        


