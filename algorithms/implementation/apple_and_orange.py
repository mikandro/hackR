def countApplesAndOranges(s,t,a,b, apples, oranges):
    house = range(s, t+1)
    print(len([a + x for x in apples if a+x >= house[0] and a+x <= house[-1]]))
    print(len([b + x for x in oranges if b+x >= house[0] and b+x <= house[-1]]))


if __name__ == "__main__":
    apples = [-2,2,1]
    oranges= [5, -7, -6]

    countApplesAndOranges(7, 11, 5, 15, apples, oranges)
