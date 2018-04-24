def migratoryBirds(n, ar):
   t = [[x,ar.count(x)] for x in set(ar)]
   max_val= max([a[1] for a in t])
   return min([b[0] for b in t if b[1] == max_val])


n = 6
ar = [1, 4, 4, 4, 5, 3,3,3, 2,2,2]
result = migratoryBirds(n, ar)
print(result)

