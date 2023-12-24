from collections import defaultdict
from typing import Set, DefaultDict, List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        children = defaultdict(list)
        for a, b in edges:  # bidirectional edges
            children[a].append(b)
            children[b].append(a)

        def root_tree(node: int, visited: Set[int], tree: DefaultDict[int, List[int]]) -> None:
            visited.add(node)
            for child in children[node]:
                if child not in visited:
                    tree[node].append(child)
                    root_tree(child, visited, tree)
    
        tree = defaultdict(list)  
        root_tree(0, set(), tree)

        def calculate_max_product(arr: List[int]) -> int:
            if len(arr) < 3:
                return 1
            else:
                return max(0, arr[0] * arr[1] * arr[2], arr[0] * arr[-1] * arr[-2])

        def merge_arrays(a: List[int], b: List[int]) -> List[int]:
            ret = []
            while a and b:
                ret.append(a.pop() if a[-1] < b[-1] else b.pop())
            while a:
                ret.append(a.pop())
            while b:
                ret.append(b.pop())
            return ret[::-1]  
        
        def truncate_array(arr: List[int]) -> List[int]:
            if len(arr) >= 6:
                return arr[:3] + arr[-3:]
            else:
                return arr
        
        coins = [0] * len(cost)
        def dfs(node):
            if not tree[node]:
                coins[node] = 1
                return [cost[node]], 1
            else:
                subarray = [cost[node]]
                for child in tree[node]:
                    subarray = truncate_array(merge_arrays(dfs(child).__getitem__(0), subarray))

                coins[node] = calculate_max_product(subarray)
                return [subarray, coins[node]]
        
        dfs(0)
        return coins