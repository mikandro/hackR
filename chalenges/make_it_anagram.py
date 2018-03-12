w1 = 'uvbaisufbashv'
w2 = 'aygieyabdadod'

total = 0
print [i for i in w1 if not i[0] in w2], [i for i in w2 if not i[0] in w1]
diff = lambda l1,l2: [x for x in l1 if x not in l2]
diff2 = lambda l1,l2: filter(lambda x: x not in l2, l1)
# print list(set(w1).symmetric_difference(set(w2)))

print sum([w1.count(x) + w2.count(x) for x in list(set(w1).symmetric_difference(set(w2)))])

print map(lambda a: w1.count(a) + w2.count(a), list(set(w1).symmetric_difference(set(w2))))


for letter in "abcdefghijklmnopqrstuvwxyz":
    total += sum([w1.count(letter) + w2.count(letter) if letter in list((set(w1) - set(w2)) + (set(w2)- set(w1))) else 0])
print total