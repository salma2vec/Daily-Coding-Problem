class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        prev = ['']
        prev.extend(
            str2[:j + 1]
            for j in range(m)
        )

        for i, a in enumerate(str1, 1):
            current = [str1[:i]]
            for j, b in enumerate(str2, 1):
                if a == b:
                    result = prev[j - 1] + a
                else:
                    x = prev[j]
                    y = current[-1]
                    if len(x) <= len(y):
                        result = x + a
                    else:
                        result = y + b
                current.append(result)
            prev = current
        
        return prev[-1]