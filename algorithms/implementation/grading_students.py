def multiple_of_5(num):
    if num%5 == 0:
        return num
    else:
        num +=1
        return multiple_of_5(num)

def solve(n, grades):
    result = []
    for i in grades:
        if i >= 38:
            t = multiple_of_5(i)
            if t - i < 3:
                result.append(t)
            else:
                result.append(i)
        else:
            result.append(i)
    return result

n = 4
grades = [73, 67, 38, 33]

result = solve(n, grades)

print "\n".join(map(str, result))
