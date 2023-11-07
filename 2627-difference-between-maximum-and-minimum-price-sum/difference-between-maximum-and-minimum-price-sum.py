class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        rtl = [[] for _ in range(n)]

        def traverse1(node, parent):
            for nei in graph[node]:
                if nei == parent: continue
                traverse1(nei, node)
                
                child = rtl[nei][-1] 
                rtl[node].append(child + price[node])
                
            if not rtl[node]:
                rtl[node].append(price[node])
            
            rtl[node].sort()
            rtl[node] = rtl[node][-2:]  # keep at most 2 entry, we dont need more
            
        traverse1(0, -1)
        
        ans = 0

        def traverse2(node, parent):
            if parent != -1:
                if len(rtl[parent]) == 1:
                    rtl[node].append(price[parent] + price[node])
                else:
                    if rtl[node][-1] + price[parent] == rtl[parent][-1]: 
                        rtl[node].append(rtl[parent][-2] + price[node])
                    else:
                        rtl[node].append(rtl[parent][-1] + price[node])
            
            rtl[node].sort()
            for nei in graph[node]:
                if nei == parent:
                    continue
                
                traverse2(nei, node)
            
        traverse2(0, -1)
        return max(rtl[i][-1] - price[i] for i in range(n))
                
        