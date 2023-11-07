class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        
        h = set(tuple(x) for x in guesses)
        
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        @cache
        def rec(p, pp):
            r = 0
            for q in g[p]:
                if q == pp: continue
                if (p, q) in h:
                    r += 1
                r += rec(q, p)
            return r
        
        r = 0
        for i in range(n):
            if rec(i, i) >= k:
                r += 1
        return r        