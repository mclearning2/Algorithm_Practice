from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        e = dict()
        g = defaultdict(list)
        for (A, B), V in zip(equations, values):
            g[A].append(B)
            e[(A, B)] = V
            e[(B, A)] = 1/V
        
        answer = []
        for q in queries:
            start, goal = q
            if start not in g:
                answer.append(-1.0)
                continue
            
        def dfs(node, start, goal, val = 1.0):
            for next_nodes in g[node]:
                val *= e[(node, next_nodes)]
                return dfs(next_nodes, start, goal, val)
            else: # g[node] is None
                return val
        
        return answer
            
