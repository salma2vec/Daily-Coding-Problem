func findDiagonalOrder(mat [][]int) []int {
    if len(mat) == 0 || len(mat[0]) == 0 {
        return []int{}
    }

    m, n := len(mat), len(mat[0])
    diagonals := make(map[int][]int)

    for row := 0; row < m; row++ {
        for col := 0; col < n; col++ {
            diagonals[row+col] = append(diagonals[row+col], mat[row][col])
        }
    }

    result := make([]int, m*n)
    idx := 0

    for k := 0; k <= m+n-2; k++ {
        if k%2 == 0 {
            for i := len(diagonals[k]) - 1; i >= 0; i-- {
                result[idx] = diagonals[k][i]
                idx++
            }
        } else {
            for i := 0; i < len(diagonals[k]); i++ {
                result[idx] = diagonals[k][i]
                idx++
            }
        }
    }

    return result
}
