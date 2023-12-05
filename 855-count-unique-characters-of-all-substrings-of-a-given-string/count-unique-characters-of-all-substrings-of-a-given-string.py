class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        res_temp = 0
        dic = defaultdict(int)
        dic_dc = defaultdict(int)
        for i, ch in enumerate(s):
            res_temp += i + 1 - dic[ch]*2 + dic_dc[ch]
            dic_dc[ch], dic[ch] = dic[ch], i+1
            res += res_temp
        return res

