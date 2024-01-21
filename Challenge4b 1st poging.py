# Escape pods.txt
# additional testcases from http://www.cs.ust.hk/mjg_lib/Classes/COMP572_Fall07/Project/maxflow_test.txt
# https://en.wikipedia.org/wiki/Ford–Fulkerson_algorithm
# https://en.wikipedia.org/wiki/Edmonds–Karp_algorithm
# https://en.wikipedia.org/wiki/Schulze_method
# https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm

def solution(entrances, exits, path):
    # Your code here
    mx=0
    route=[]
    total=0
    size=len(path[0])
    while True:
        widest_paths, routes=schulze(path,size)
        for i in entrances:
            for j in exits:
                if widest_paths[i][j]>mx:
                    mx=widest_paths[i][j]
                    route=FWPath(i,j,routes)
        if mx==0:
            return total
        for i in range(len(route)-1):
            path[route[i]][route[i+1]]-=mx
        total+=mx
        mx=0
        route=[]

def schulze(path, size):
    p=[[0 for i in range(size)] for j in range(size)]
    nxt=[[None for i in range(size)] for j in range(size)]
    d=path
    for i in range(size):
        for j in range(size):
            if i!=j:
                if d[i][j]>d[j][i]:
                    p[i][j]=d[i][j]
                if d[i][j]>0:
                    nxt[i][j]=j
            else:
                nxt[i][j]=i
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if p[i][j] < min(p[i][k], p[k][j]):
                    p[i][j]=min(p[i][k],p[k][j])
                    nxt[i][j]=nxt[i][k]
    return p, nxt

def FWPath(start, end, nxt):
    if nxt[start][end]==None:
        return []
    p=[start]
    while start!=end:
        start=nxt[start][end]
        p.append(start)
    return p

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
                
    
