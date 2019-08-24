'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''

# 207. Course Schedule 문제와 하다. Topology order DFS version
# DAG(Directed Acyclic Graph)인지만 검사했던 위 문제와 달리 순서도 정해줘야 한다.
# DFS를 사용해 차수가 0인 지점부터 마지막 노드까지 쭉 읽어 list에 저장한 뒤 거꾸로 반환해야하지만
# 난 애초에 읽는 순서를 반대로 해서 list를 그대로 반환한다.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        node = ["not_visited" for _ in range(numCourses)]
        ordered = []
        
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
                ordered.append(c)
                return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        else:
            return ordered
