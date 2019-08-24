from itertools import permutations
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda : defaultdict(lambda: float('inf')))
        for (f, t), v in zip(equations, values):
            graph[f][t] = v
            graph[t][f] = 1/v
            graph[f][f] = 1.0
            graph[t][t] = 1.0
            
        for s, m, e in permutations(graph, 3):
            if m in graph[s] and e in graph[m]:
                graph[s][e] = graph[s][m] * graph[m][e]
        
        l = list()
        for f, t in queries:
            if graph[f][t] == float('inf'):
                l.append(-1.0)
            else:
                l.append(graph[f][t])
    
        return l
