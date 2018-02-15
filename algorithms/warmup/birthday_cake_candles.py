def birthdayCakeCandles_v2(n, arr):
    hi_count = 0
    highest_first_index = 0
    highest_value = max(arr)
    try:
        highest_first_index = arr.index(highest_value)
    except:
        print 0

    hi_count +=1

    i = highest_first_index
    while i < n:
        try:
            h_i = arr[i+1:].index(highest_value)
            i += 1 + h_i
            hi_count +=1
        except:
            break


    return hi_count



def birthdayCakeCandles(n, ar):
    highest = max(ar)
    return len([x for x in ar if x == highest])

n = 4
ar = [9,2,1,9, 5,5,3,9,2,2,9,1,9,8,9]
result = birthdayCakeCandles_v2(len(ar), ar)
print(result)
