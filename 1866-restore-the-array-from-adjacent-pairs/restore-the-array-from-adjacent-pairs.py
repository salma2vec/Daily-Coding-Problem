class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        adj_dict = defaultdict(deque)
        for pair in adjacentPairs:
            adj_dict[pair[0]].append(pair[1])
            adj_dict[pair[1]].append(pair[0])

        start = 0
        for num, neighbors in adj_dict.items():
            if len(neighbors) == 1:
                start = num
                break

        res = deque()
        res.append(start)

        while adj_dict[start]:
            neighbor = adj_dict[start].popleft()
            adj_dict[neighbor].remove(start)
            res.append(neighbor)
            start = neighbor

        return list(res)        