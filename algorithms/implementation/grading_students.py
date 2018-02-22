def multiple_of_5(num):
    if num%5 == 0:
        return num
    else:
        num +=1
        return multiple_of_5(num)

def solve(n, grades):
    # for grade in grades:
    # if grade < 40:
    #     print grade
    # else:
    t = [ x for x in [y if y%5==0 else multiple_of_5(y) for y in grades]]
    print t

n = 4
grades = [73, 67, 38, 33]

result = solve(n, grades)

print "\n".join(map(str, result))
