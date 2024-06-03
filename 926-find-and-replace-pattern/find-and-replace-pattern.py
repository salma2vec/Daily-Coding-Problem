class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            char_map = {}
            rev_map = {}
            for c1, c2 in zip(pattern, word):
                if c1 not in char_map:
                    if c2 in rev_map:
                        return False
                    char_map[c1] = c2
                    rev_map[c2] = c1
                elif char_map[c1] != c2:
                    return False
            return True
        
        return [word for word in words if len(word) == len(pattern) and match(word)]