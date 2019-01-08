from random import randint

def array_manipulation(n, queries):
    il = [0 for i in xrange(n)]
    print il
    for q in queries:
        for j in xrange(q[0], q[1]+1):
            il[j-1]+=q[2]


    return max(il)

n = 5
queries = [[1,2,100], [2,5,100], [3,4,100]]

result = array_manipulation(n, queries)
print "res: %i" %result