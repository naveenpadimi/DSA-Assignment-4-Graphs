# 1.Breadth First Traversal for a Graph

from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):

		visited = [False] * (max(self.graph) + 1)

	
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:

			
			s = queue.pop(0)
			print(s, end=" ")

			
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
	" (starting from vertex 2)")
g.BFS(2)
# 2.Depth First Traversal for a Graph

from collections import defaultdict

class Graph:

	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):

		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	def DFS(self, v):

		visited = set()

		self.DFSUtil(v, visited)

if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	g.DFS(2)

# 3.Count the number of nodes at given level in a tree using BFS

import queue

def printLevels(graph, V, x):

	level = [None] * V
	marked = [False] * V

	que = queue.Queue()

	que.put(x)

	level[x] = 0

	marked[x] = True

	while (not que.empty()):

		x = que.get()

		for i in range(len(graph[x])):

			b = graph[x][i]

			if (not marked[b]):

				que.put(b)

				level[b] = level[x] + 1

				marked[b] = True

	print("Nodes", " ", "Level")
	for i in range(V):
		print(" ", i, " --> ", level[i])

if __name__ == '__main__':

	V = 8
	graph = [[] for i in range(V)]

	graph[0].append(1)
	graph[0].append(2)
	graph[1].append(3)
	graph[1].append(4)
	graph[1].append(5)
	graph[2].append(5)
	graph[2].append(6)
	graph[6].append(7)

	printLevels(graph, V, 0)

# 4. Count number of trees in a forest



adj_list = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3, 5],
    5: [4]
}
def num_connected_components(adj_list):
    visited = set()
    num_components = 0
    for node in adj_list:
        if node not in visited:
            stack = [node]
            while stack:
                curr_node = stack.pop()
                if curr_node not in visited:
                    visited.add(curr_node)
                    stack.extend(adj_list[curr_node])
            num_components += 1
    return num_components

num_trees = num_connected_components(adj_list)
print(num_trees)

#  5.Detect Cycle in a Directed Graph

def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [5],
    4: [1],
    5: [6],
    6: [3]
}

if has_cycle(graph):
    print("The graph has a cycle")
else:
    print("The graph does not have a cycle")
