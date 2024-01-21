def solution(times, times_limit):
    size = len(times)
    if size <3:
        # No bunnies to be found
        return [] # No cases?
    shortest_paths=FW(times, size)
    if min([shortest_paths[i][i] for i in range(size)]) < 0:
        # if there's negative numbers on the diagonal of the floyd-warshall
        # matrix, then there's a negative cycle that we can exploit to rescue all
        # the bunnies
        return list(range(size-2)) #Case 7?
    success=[]
    for rescue in range(size-2, -1, -1):
        # First we'll try to rescue all the bunnies, then 1 less each loop
        for route in permutations(range(1,size -1), rescue):
            if isdoable(shortest_paths, [0]+list(route)+[size-1], times_limit):
                success.append(list(route))
        if len(success)>0:
            break
    #print(success)
    lowest_IDs=min(success, key=sum)
    return [i-1 for i in sorted(lowest_IDs)]
    

def FW(times, size):
    # Returns a matrix of the shortest paths using Floyd Warshall
    shortpath=[row[:] for row in times]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if shortpath[i][j] > shortpath[i][k]+shortpath[k][j]:
                    shortpath[i][j]=shortpath[i][k]+shortpath[k][j]
    return shortpath

def isdoable(times, route, time_limit):
    #Checks if a proposed route is doable under the time limit
    time=0
    for i in range(len(route)-1):
        time+=times[route[i]][route[i+1]]
    return time <= time_limit
    
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def permutations(iterable, r=None):
    # Looks like imports aren't working on the google foobar challenge
    # so copied the itertools.permutations source
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
