func findDiagonalOrder(mat [][]int) []int {
    x, y := 0, 0
    rows := len(mat) - 1
    cols := len(mat[0]) - 1
    res := []int{}
    up := true
    for {
        if x + y > rows + cols {
            break
        }
        res = append(res, mat[x][y])

        if up && y >= cols { 
            up = false
            x++
        } else if up && x <= 0 { 
            up = false
            y++
        } else if !up && x >= rows {
            up = true
            y++
        } else if !up && y <= 0 { 
            up = true
            x++
        } else if up { 
            x--
            y++
        } else {
            x++
            y--
        }
    }
    return res
}
