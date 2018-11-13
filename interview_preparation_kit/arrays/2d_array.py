# arr = [ 1,1,1,0,0,0,
#         0,1,0,0,0,0,
#         1,1,1,0,0,0,
#         0,0,2,4,4,0,
#         0,0,0,2,0,0,
#         0,0,1,2,4,0]

# arr = [
#     -1, -1, 0, -9, -2, -2,
# -2, -1, -6, -8, -2, -5,
# -1, -1, -1, -2, -3, -4,
# -1, -9, -2, -4, -4, -5,
# -7, -3, -3, -2, -9, -9,
# -1, -3, -1, -2, -4, -5
# ]

arr = [3 , 7 , -3, 0 , 1 , 8,
       1 , -4, -7, -8, -6, 5,
       -8, 1 , 3 , 3 , 5 , 7,
       -2, 4 , 3 , 1 , 2 , 7,
       2 , 4 , -5, 1 , 8 , 4,
       5 , -7, 6 , 5 , 2 , 8]

def hourglass_sum(arr):
    hg_max = None
    for i in range(0,22):
        # print i
        if i % 6 != 4 and i%6 != 5:
            print "IIIII: {}".format(i)
            print "{}\n    {}\n{}".format(arr[i: i+3] , arr[i + 7] , arr[i + 12: i + 15])
            tmp_hg_max = sum(arr[i: i+3]) + arr[i + 7] + sum(arr[i + 12: i + 15])
            print "i: {}, max: {}".format(i, tmp_hg_max)
            if tmp_hg_max > hg_max:
                hg_max = tmp_hg_max
            print "\n\n"
    return hg_max


print hourglass_sum(arr)