def divisibleSumPairs(n, k, ar):
    r = 0
    for i,x in enumerate(ar):

        for j,y in enumerate(ar[i+1:n], i+1):
            print i,j
            s = ar[i] + ar[j]
            print ar[i],ar[j],ar[i+1:n],s
            if s % k == 0:
                r +=1
    return r


n, k = [6,3]
ar = [1, 3, 2, 6, 1, 2]
result = divisibleSumPairs(n, k, ar)
print(result)
