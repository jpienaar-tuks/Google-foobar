# Find the access codes.txt

def solution(l):
# Naive brute force solution. Too slow
    t=0
##    c=0
    length=len(l)
    for ii in range(length-2):
        for ij in range(ii+1, length-1):
            if l[ij]%l[ii]==0:
                for ik in range(ij+1, length):
                    #c+=1
                    if l[ik]%l[ij]==0:
                        t+=1
##    print('Did {} comparisons'.format(c))
    return t

def solution2(l):
# Inspired by https://github.com/dblVs/Google-foobar/blob/master/find_the_access_codes.py
# Final submitted solution
    t=0
    for i in range(1,len(l)-1):
        divisors = len(filter(lambda x: l[i]%x==0,l[:i])) #Number of divisors to the left
        multiples = len(filter(lambda x: x%l[i]==0,l[i+1:])) #Number of multiples to the right
        t+=divisors*multiples
    return t

if __name__=='__main__':
    assert solution([1, 2, 3, 4, 5, 6])==3
    assert solution([1,1,1])==1

