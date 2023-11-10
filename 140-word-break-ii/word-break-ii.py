class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)

        @lru_cache(maxsize=None)
        def wordBreakDP(start):
            if start == n:
                return [""]
            sentences = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in wordSet:
                    next_sentences = wordBreakDP(end)
                    for sentence in next_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            return sentences

        return wordBreakDP(0)