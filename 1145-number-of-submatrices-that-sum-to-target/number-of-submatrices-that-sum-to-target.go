func numSubmatrixSumTarget(matrix [][]int, target int) int {
    m, n := len(matrix), len(matrix[0])
    res := 0

    for l := 0; l < n; l++ {
        sums := make([]int, 105)
        for r := l; r < n; r++ {
            for i := 0; i < m; i++ {
                sums[i] += matrix[i][r]
            }
            for i := 0; i < m; i++ {
                sum := 0
                for j := i; j < m; j++ {
                    sum += sums[j]
                    if sum == target {
                        res++
                    }
                }
            }
        }
    }

    return res
}