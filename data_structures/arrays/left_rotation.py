n = 5
d = 5
a = [6,7,8,9,10]

def rotLeft(a,d):
    tmp = list(range(0,n))
    if n == d :
        return a
    else:
        for key, val in enumerate(a):
            if n-d+key == n:
                print("==n", key, val)
                tmp[0] = val
            elif n-d+key < n:
                print("<n", key,val)
                tmp[n-d+key] = val
            else:
                print(">n", key, val)
                tmp[(n-d+key)-n] = val


        return tmp

# print(a)

res = rotLeft(a,d)
print(res)