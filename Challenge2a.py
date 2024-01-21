# Lucky lambs.txt
def solution(total_lambs):
    # Your code here
    #import math

    if total_lambs <=3:
        return 0
    else:
        fibo=[1,1]
        while True:
            if sum(fibo)>total_lambs:
                lg = len(fibo)-1
                break
            fibo.append(sum(fibo[-2:]))
        
        pow2=[1]
        while True:
            if sum(pow2)>total_lambs:
                mg = len(pow2)-1
                break
            pow2.append(2**len(pow2))
    
        #mg = math.floor(math.log(total_lambs+1,2))
        
        return abs(mg-lg)
            
if __name__ == '__main__':
    assert solution(143)==3
    assert solution(10)==1

