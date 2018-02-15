import sys


def add_stair(i, n):
    l = (n-1-i) * ' '
    s = (i+1) * '#'
    print l + s


def staircase(n):
    for i in range(0, n):
        add_stair(i, n)

if __name__ == "__main__":
    # n = int(raw_input().strip())
    n = 6
    staircase(n)
