import sys, string, math
ss1,ss2 = input().split()
mi1 = len(ss1)
mi2 = len(ss2)
if mi2 > mi1 :
    j = 0
    while j<mi1 and ss1[j] == ss2[j] :
        j += 1
    print(mi2-j)
elif mi2 == mi1 :
    j = 0
    while j<m2 and ss1[j] == ss2[j] :
        j += 1
    print(mi2-j)
else :
    j = 0
    while j<mi2 and ss1[j] == ss2[j] :
        j += 1
    s31 = ss1[j:]
    s32 = ss2[j:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(mi1-j-k)
