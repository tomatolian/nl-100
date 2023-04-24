N=int(input())
with open('popular-names.txt','r') as f:
    n=len(f)
    print(*f.readlines()[-N:])