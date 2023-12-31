class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        li = []
        li1 = []
        li2 = []
        for i in range(len(s)):
            if s.count(s[i])>1 and s[i] not in li:
                li.append(s[i])
                li1.append(i)
        for j in li:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == j:
                    li2.append(i)
                    break
        li3=[]
        for i in range(len(li1)):
            li3.append(li2[i] - li1[i] - 1)
        if len(li) > 0:
            return max(li3)
        else:
            return -1        