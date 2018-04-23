import sys

def solve(n, s, d, m):
    matches = 0
    # print s,d,m
    for i,v in enumerate(s):
        piece_sum = sum(s[i: i+m])
        print i, v, piece_sum
        if piece_sum == d:
            matches +=1

    return matches

n = 5
s = [1,2,1,3,2]
d, m = 3,2
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
