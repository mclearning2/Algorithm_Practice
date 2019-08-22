'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

# directed graph, 자신 위치에서 한 방향으로 쭉 가다가 어떤 노드를 만났을 경우는 두 가지이며, 이를 구분해야 한다.
# 1. 다른 node에서 시작해서 쭈욱 지나간 경우. 이 것은 cycle이 아니라 그저 탐색 중에 한 번 방문한 상황.
# 2. 자신이 갔던 길을 다시 돌아온 경우. 이 경우는 cycle이다.
# cycle이 된 경우는 무조건 canFinish의 반환이 바로 False가 되도록 한다.
# cycle이 아닌 경우는 탐색했다는 흔적을 남겨놓는다. 다른 곳에서 탐색하다가 이곳을 지나가는 경우 이미 탐색 완료한 지점이니 True가 되도록 한다.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        node = ["not_visited" for _ in range(numCourses)]
        
        for c, p in prerequisites:
            graph[c].append(p)
        
        def dfs(c):
            
            if node[c] == "unsafe":
                return False
            elif node[c] == "safe":
                return True
            elif node[c] == "not_visited":
                
                node[c] = "unsafe"
                
                for p in graph[c]:
                    if not dfs(p):
                        return False
                    
                node[c] = "safe"
                return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        else:
            return True
