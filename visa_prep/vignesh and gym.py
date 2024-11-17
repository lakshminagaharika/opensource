x,y,z=list(map(int,input().split()))
if z<x:
    print("0")
elif z<(x+y):
    print("1")
else:
    print("2")
