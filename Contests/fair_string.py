def flip(ch):
    if ch=='0':
        return '1'
    else:
        return '0'

def startwith(s, expected, n, cost):
    count = 0
    for i in range(n):
        if s[i] != expected:
            count += cost[i]
        expected = flip(expected)
    return count

def startwith2(s, expected, n, cost):
    count = 0
    for i in range(0,n,2):
        if s[i] != expected:
            count += cost[i]
        if s[i+1] != expected:
            count += cost[i+1]
        expected = flip(expected)
    return count

class Solution:
    def solve(self,n,s,a):
        #code here
        a1 = startwith(s, '0', n, a)
        a2 = startwith(s, '1', n, a)
        a3 = startwith2(s, '0', n, a)
        a4 = startwith2(s, '1', n, a)
        return min(a1,a2,a3,a4)
