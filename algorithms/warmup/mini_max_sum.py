def mini_max_sum_v2(arr):

    print reduce(lambda x,y: x+y, arr) - max(arr), reduce(lambda x,y: x+y, arr) - min(arr)


def mini_max_sum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_val = total_sum - min(arr)

    print min_sum, max_val

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    mini_max_sum(arr)
