n = 9
ar = [10, 10, 10,  20, 20, 10, 10, 30, 50, 10, 20]

collors = set(ar)

print(collors)

pairs = 0
for collor in collors: 
    occ = ar.count(collor)
    pairs += occ//2

print(pairs)
