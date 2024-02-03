func maxSumAfterPartitioning(arr []int, k int) int {
    ln := len(arr)
    temp := make([]int, ln + 1)
    for i := 1; i <= ln; i++ {
        mx := 0
        for j := i; j > max(0, i - k); j-- {
            mx = max(mx, arr[j - 1])
            temp[i] = max(temp[i], temp[j - 1] + mx * (i - j + 1))
        }
    }
    return temp[ln]
}