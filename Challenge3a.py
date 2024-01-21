#The grandest staircase of them all.txt

## Reading on the internet spurred me to look into the "partition problem", and
## in particular distinct/odd partitions.
## Below solution based on https://mathworld.wolfram.com/PartitionFunctionP.html
## eq 34 and trying to determine the coefficients for n terms

def solution(n):
# storing terms as {exponent, coefficient}, so
#(1+x) becomes {0:1, 1:1}
#(1+x**2) becomes {0:1, 2:1} etc.
        termmult1=lambda x, y: termmult(x,y,n)
        results=reduce(termmult1,[{0:1, i:1} for i in range(n)]).values()
        return results[n]

def termmult(t1, t2, n):
        r={}
        for key1, value1 in t1.items():
                for key2, value2 in t2.items():
                        # upper limit from problem is 200 so we only care for coefficients of exponents less than 200
                        if key1+key2 <= n+5:
                                if key1+key2 in r:
                                        r[key1+key2]+=value1*value2
                                else:
                                        r[key1+key2]=value1*value2
        return r

if __name__=='__main__':
        assert solution(3)==1
        assert solution(200)==487067745
