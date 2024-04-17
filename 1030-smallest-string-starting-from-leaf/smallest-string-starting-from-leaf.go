func smallestFromLeaf(root *TreeNode) string {
    var result string
    var currentPath []rune

    dfs(root, &currentPath, &result)

    return result
}

func dfs(node *TreeNode, currentPath *[]rune, result *string) {
    if node == nil {
        return
    }

    *currentPath = append(*currentPath, rune(node.Val)+'a')

    if node.Left == nil && node.Right == nil {
        pathStr := string(reverse(*currentPath))
        if *result == "" || pathStr < *result {
            *result = pathStr
        }
    }

    dfs(node.Left, currentPath, result)
    dfs(node.Right, currentPath, result)

    *currentPath = (*currentPath)[:len(*currentPath)-1]
}

func reverse(runes []rune) []rune {
    reversed := make([]rune, len(runes))
    for i, j := 0, len(runes)-1; i <= j; i, j = i+1, j-1 {
        reversed[i], reversed[j] = runes[j], runes[i]
    }
    return reversed
}