class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree= [0] * numCourses

        result = []
        mapper = defaultdict(list)

        for ai, bi in prerequisites:
            mapper[bi].append(ai)
            indegree[ai] += 1


        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while(q):
            node = q.popleft()
            result.append(node)
            for neigh in mapper[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        if len(result) == numCourses:
            return result
        return []                