# Running with bunnies.txt

#from itertools import permutations

def solution(times, time_limit):
    size = len(times)
    if size <3:
        # No bunnies to be found
        return [] # No cases?
    shortest_paths=FW(times, size)
    if min([shortest_paths[i][i] for i in range(size)]) < 0:
        # if there's negative numbers on the diagonal of the floyd-warshall
        # matrix, then there's a negative cycle that we can exploit to rescue all
        # the bunnies
        return list(range(size-2)) # Case 7?
    success=[]
    for rescue in range(size-2, -1, -1):
        # First we'll try to rescue all the bunnies, then 1 less each loop
        for route in permutations(range(1,size -1), rescue):
            if isdoable(shortest_paths, [0]+list(route)+[size-1], time_limit):
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

if __name__=='__main__':
    # Additional testcases from https://github.com/FoxHub/Google-FooBar/blob/master/Level-4/foobar_4-2_running_with_bunnies.py
    case1 = [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    print("\n\nCase 1: Provided test case 1.\nTime limit: 3")
    for row in case1:
        print(row)
    print("\n  Expected: [0, 1]\nCalculated: {}".format(str(solution(case1, 3))))

    print("\n\nCase 2: Provided test case 2.\nTime limit: 1")
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    for row in case2:
        print(row)
    print("\n  Expected: [1, 2]\nCalculated: {}".format(str(solution(case2, 1))))

    print("\n\nCase 3: Infinite negative cycle.\nTime limit: -500")
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print(row)
    print("\n  Expected: [0, 1, 2]\nCalculated: {}".format(str(solution(case3, -500))))

    print("\n\nCase 4: Max bunnies. None rescuable.\nTime limit: 1")
    case4 = [[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]
    for row in case4:
        print(row)
    print("\n  Expected: []\nCalculated: {}".format(str(solution(case4, 1))))

    print("\n\nCase 5: One bunny.\nTime limit: 2")
    case5 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    for row in case5:
        print(row)
    print("\n  Expected: [0]\nCalculated: {}".format(str(solution(case5, 2))))

    print("\n\nCase 6: Multiple revisits.\nTime limit: 10")
    case6 = [[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]]
    for row in case6:
        print(row)
    print("\n  Expected: [0, 1]\nCalculated: {}".format(str(solution(case6, 10))))

    print("\n\nCase 7: Multiple Revisits 2.\nTime limit: 5")
    case7 = [[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]]
    for row in case7:
        print(row)
    print("\n  Expected: [0, 1]\nCalculated: {}".format(str(solution(case7, 5))))

    print("\n\nCase 8: Time travel.\nTime limit: 1")
    case8 = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    for row in case8:
        print(row)
    print("\n  Expected: [0, 1, 2]\nCalculated: {}".format(str(solution(case8, 1))))

    print("\n\nCase 9: No bunnies.\nTime limit: 1")
    case9 = [[2, 2],
             [2, 2]]
    for row in case9:
        print(row)
    print("\n  Expected: []\nCalculated: {}".format(str(solution(case9, 1))))

    print("\n\nCase 10: Backwards bunny path.\nTime limit: 6")
    case10 = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
    for row in case10:
        print(row)
    print("\n  Expected: [0, 1, 2]\nCalculated: {}".format(str(solution(case10, 6))))
    
    
