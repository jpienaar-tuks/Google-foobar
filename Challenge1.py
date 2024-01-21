# Re-ID.txt
def solution(i):
    # Your code here
    primes=[2,3,5]
    lambda_str='235'
    j=6
    while len(lambda_str)<10005:
        flag=True
        for prime in primes:
            if j%prime==0:
                flag=False
                break
        if flag:
            primes.append(j)
            lambda_str+=str(j)
        j+=1
        #print(lambda_str)
    return lambda_str[i:i+5]

solution(1)
