INF = 999
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj):
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0
    selected = [False] * n

    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')
        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

        print(': ', dist)
    print()

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [ [0, 25, INF,	12,	INF, INF, INF],
           [25, 0, 10, INF,	15, INF, INF],
           [INF, 10, 0, INF, INF, INF, 16],
           [12, INF, INF, 0, 17, 37, INF],
           [INF, 15, INF, 17, 0, 19, 14],
           [INF, INF, INF, 37, 19, 0, 42],
           [INF, INF, 16, INF, 14, 42, 0] ] 
print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)