def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'

    if abs(x2-x2)%abs(v1-v2) == 0:
        return 'YES'
    else:
        return 'NO'

# result = kangaroo(0, 2, 5, 4)
result = kangaroo(0, 3, 4, 2)
# result = kangaroo(2081, 8403, 9107, 8400)
print(result)