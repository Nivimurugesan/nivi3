from itertools import combinations
zi,ab=map(int,input().split())
bb=len(str(zi))
x1=list(combinations(str(zi),bb-ab))
x1=(sorted(x1))
y1="".join(x1[0])
print(y1)
