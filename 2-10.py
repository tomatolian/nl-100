file='popular-names.txt'

f=open(file,'r')
n=len(f.readlines())
f.close()
print(n)

# wc -l popular-names.txt