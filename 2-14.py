N=int(input())
with open('popular-names.txt','r') as f:
    print(*f.readlines()[:N])

#head -n N popular-names.txt