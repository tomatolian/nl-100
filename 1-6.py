def ngram(N,w):
  ans=[]
  lis=w.split(' ')
  for i in range(len(lis)-1):
    ans.append(lis[i:i+N])
  return ans
t='paraparaparadise'
t1='paragraph'
x=ngram(2,t)
y=ngram(2,t1)
print(x,y)