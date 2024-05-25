func wordBreak(s string, wordDict []string) []string {
    wordSet := make(map[string]bool)
    for _, word := range wordDict {
        wordSet[word] = true
    }

    var (
        sentences []string
        sentence  []string
        dfs       func(int)
    )

    dfs = func(start int) {
        if start == len(s) {
            sentences = append(sentences, strings.Join(sentence, " "))
            return
        }

        for end := start + 1; end <= len(s); end++ {
            word := s[start:end]
            if wordSet[word] {
                sentence = append(sentence, word)
                dfs(end)
                sentence = sentence[:len(sentence)-1]
            }
        }
    }

    dfs(0)
    return sentences
}
