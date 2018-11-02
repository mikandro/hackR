c = [0,0,0,0,1,0]
#c = [0,0,1,0,0,1,0]

jumps = 0
pace = 1

for cloud in c:
    print(cloud)
#    next_c = c[i+1]
    if cloud == 1 or pace ==2:
        jumps +=1
        pace = 1
    else:
        pace +=1

print(jumps)
