type pair struct {
    row int
    col int
}

func uniquePathsIII(grid [][]int) int {
    empty_square := 0
    var start pair
    var end pair
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[i]);j++{
            if grid[i][j] == 1{
                 start = pair{i,j}
            }else if grid[i][j]==2{
                end = pair{i,j}
            }
            if grid[i][j] != -1{
                empty_square+=1
            }
        }
    }
            
    visited := map[pair]bool{}
    visited[start] = true
    empty_square-=1
    return dfs(start,end,grid,empty_square,&visited)
}

func dfs(start,end pair,grid [][]int,empty_squre int,visited *map[pair]bool) int{
    if start == end{
        if empty_squre == 0{
            return 1
        }else{
            return 0
        }
    }
    moves := [][]int{{-1,0},{1,0},{0,-1},{0,1}}
    answer := 0
    for _,move :=range(moves){
        row := start.row+move[0]
        col := start.col+move[1]
        if 0<=row && row<len(grid) && 0<=col && col<len(grid[0]) && grid[row][col] != -1{
            curr := pair{row,col}
            if _,ok := (*visited)[curr]; ok{
                continue
            }
            empty_squre-=1
            (*visited)[curr] = true
            answer+= dfs(curr,end,grid,empty_squre,visited)
            empty_squre+=1
            delete(*visited,curr)
        }
    }
    return answer
}
