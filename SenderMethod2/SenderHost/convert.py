import more_itertools

def string2ternary(s):
    nums = []
    for i in s:
        num = ord(i.lower())-96
        if num <=0 or num >26:
            num = 0
        for j in ternary(num):
            nums.append(j)
    return nums

def ternary2string(t):
    res = ''
    for i in more_itertools.grouper(iterable=t, n=3):
        num = 0
        for n,j in enumerate(reversed(i)):
            num += j*(3**n)
        if num <=0 or num >26:
            res += " "
        else:
            num += 96
            res += chr(num)
    return(res)
        

def ternary (n, m=3):
    if n == 0:
        return [0,0,0]
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(r)
    while len(nums)<m:    
        nums.append(0)
    return reversed(nums)
