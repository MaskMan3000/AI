import queue


graph = [[0, 1, 1, 1, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 1, 0],
         [1, 1, 1, 0, 1],
         [0, 1, 0, 1, 0]]

q = queue.Queue(maxsize=6)
s = []

r_q = []
r_s = []
r_sr = []

visited_Q = [0, 0, 0, 0, 0]
visited_S = [0, 0, 0, 0, 0]
visited_Sr = [0, 0, 0, 0, 0]
Node = ['A', 'B', 'C', 'D', 'E']


def get_index(L, E):
    for i in range(len(L)):
        if(L[i] == E):
            return i


def bfs(start):
    visited_Q[start] = 1
    q.put(Node[start])
    while(q.empty() != True):
        for j in range(5):
            if(graph[start][j] == 1 and visited_Q[j] != 1):
                q.put(Node[j])
                visited_Q[j] = 1
        r_q.append(q.get())
        if(q.empty() != True):
            start = get_index(Node, q.queue[0])


def dfs(start):
    s.append(Node[start])
    visited_S[start] = 1
    while s:
        current = s.pop()
        r_s.append(current)
        for j in range(5):
            if graph[get_index(Node, current)][j] == 1 and visited_S[j] != 1:
                s.append(Node[j])
                visited_S[j] = 1


def dfs_recursive(node_index):
    visited_Sr[node_index] = 1
    r_sr.append(Node[node_index])
    for j in range(5):
        if graph[node_index][j] == 1 and visited_Sr[j] != 1:
            dfs_recursive(j)

bfs(4)
print("BFS Traversal :- " , r_q)
print('\n\n')
dfs(4)
print("DFS Traversal :- " , r_s)
dfs_recursive(4)
print("DFS Traversal :- " , r_sr)
