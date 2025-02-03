def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end = ' ')
                ST_DFS(vtx, adj, v, visited)

vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]

print('ST_DFS_AM: ', end='')
ST_DFS(vtx, edge, 0, [False] * len(vtx))
print()