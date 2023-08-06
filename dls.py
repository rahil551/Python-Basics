graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L','M'],
    'G':['N','O'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[]
}
def DLS(start,goal,path,level,maxD):
    print("current level:",level)
    print("Goal node testing for",level)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print("Goal node testing Failed")
    if level == maxD:
        return False
    print("Expanding thr current node",start)
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False
  
  
  
path = list()
print(DLS('A','H',path,0,3))
