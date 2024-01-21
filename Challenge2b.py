# Bunny prisoner Locating.txt
def solution(x,y):
    def diag(n):
        d=1
        for i in range(1,n):
            d+=i
        return d
    return str(diag(x+y-1)+x-1)

if __name__=='__main__':
    r=list(range(1,100001))
    assert solution(3,2)=='9'
    assert solution(5,10)=='96'
    

