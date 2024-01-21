# Escape pods.txt
# additional testcases from http://www.cs.ust.hk/mjg_lib/Classes/COMP572_Fall07/Project/maxflow_test.txt
# https://en.wikipedia.org/wiki/Edmonds-Karp_algorithm
# https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm
# https://en.wikipedia.org/wiki/Schulze_method
# https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm

def solution(entrances, exits, path):
    # Your code here
    path=addsupernodes(entrances, exits, path)
    size=len(path)
    return Graph(path).edmonds_karp(size-2, size-1)

def addsupernodes(entrances, exits, path):
    size=len(path)
    for row in path:
        row+=[0,0]
    source=[0 for i in range(size+2)]
    for entrance in entrances:
        source[entrance]=2000000
    path.append(source)
    path.append([0 for i in range(size+2)])
    for exit_ in exits:
        path[exit_][size+1]=2000000
    return path
    
# This class represents a directed graph using adjacency matrix representation
class Graph:
    
    def __init__(self,graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
  
    def bfs(self, s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)
         
        # Create a queue for BFS
        queue = list()
         
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
         
        # Standard BFS loop
        while queue:
            u = queue.pop(0)
         
            # Get all adjacent vertices's of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]
             
    # Returns the maximum flow from s to t in the given graph
    def edmonds_karp(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.bfs (source, sink, parent):
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow += path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow

if __name__=='__main__':
    with open('maxflow_test.txt','rt') as f:
        cases=[]
        case={}
        nextlineissize=False
        nextlineisanswer=False
        answers=[]
        size=0
        for line in f.readlines():
            if size >0:
                    case[cases[-1]].append([int(i) for i in line.split()])
                    size -=1
            if nextlineissize:
                    size=int(line)
                    nextlineissize=False
                    case[cases[-1]]=[]
            if nextlineisanswer:
                    answers.append(int(line))
                    nextlineisanswer=False
            if line[:2]=='//':
                    nextlineissize=True
                    cases.append(int(line[-2]))
            if line.lower()[:6]=='answer':
                    nextlineisanswer=True

    for c, a in zip(cases, answers):
        assert Graph(case[c]).edmonds_karp(0, len(case[c])-1) == a
    
