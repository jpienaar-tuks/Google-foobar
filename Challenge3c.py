# Fuel injection perfection.txt
def solution(n):
    n=int(n)
    steps=0
    while n!=1:
        print(n)
        if n%2==0:
            n/=2
            steps+=1
        elif n==3:
            n=2
            steps+=1
        else:
            # Either add or subtract 1. Find the option with the most zeroes
            # at the end of the binary representation as this would allow the
            # most sequential divide by two operations
            n=min([n+1, n-1], key = lambda x: bin(x).rfind('1'))
            steps+=1
    return steps

if __name__=='__main__':
    assert solution('4') == 2
    assert solution('15') == 5
