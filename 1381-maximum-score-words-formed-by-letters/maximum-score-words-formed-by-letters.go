func maxScoreWords(words []string, letters []byte, score []int) int {
    count := make([]int, 26)
    for _, letter := range letters {
        count[letter - 'a']++
    }

    wordScore := make([]int, len(words))
    wordCount := make([][]int, len(words))
    for i, word := range words {
        wordCount[i] = make([]int, 26)
        for _, c := range word {
            wordCount[i][c - 'a']++
            wordScore[i] += score[c - 'a']
        }
    }

    memo := make([]int, 1 << len(words))
    for i := range memo {
        memo[i] = -1
    }

    var dfs func(int) int
    dfs = func(mask int) int {
        if memo[mask] != -1 {
            return memo[mask]
        }
        currentCount := make([]int, 26)
        copy(currentCount, count)
        totalScore := 0
        valid := true
        for i := 0; i < len(words); i++ {
            if mask & (1 << i) != 0 {
                for j := 0; j < 26; j++ {
                    currentCount[j] -= wordCount[i][j]
                    if currentCount[j] < 0 {
                        valid = false
                        break
                    }
                }
                if !valid {
                    break
                }
                totalScore += wordScore[i]
            }
        }
        if !valid {
            memo[mask] = 0
            return 0
        }
        maxScore := totalScore
        for i := 0; i < len(words); i++ {
            if mask & (1 << i) == 0 {
                maxScore = max(maxScore, dfs(mask | (1 << i)))
            }
        }
        memo[mask] = maxScore
        return maxScore
    }

    return dfs(0)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
