graph= {'1' : ['2','4'],
       '3' : ['5','2','4'],
       '5' : ['3','7','6'],
       '2' : ['1','3'],
       '4' : ['1','3'],
       '7' : [],
       '6':[]}
visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)
dfs(visited,graph,'1')