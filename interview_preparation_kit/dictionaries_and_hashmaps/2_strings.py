s1= 'hell'
s2= 'word'

def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    for i in s1:
        if i in s2:
            return 'YES'
    return 'NO'

print twoStrings(s1, s2)