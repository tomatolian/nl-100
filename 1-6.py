def ngram(N,w):
  ans=[]
  lis=list(w)
  for i in range(len(lis)-1):
    ans.append(''.join(lis[i:i+N]))
  return ans
t='paraparaparadise'
t1='paragraph'
x=ngram(2,t)
y=ngram(2,t1)
print('x:',bool('se' in x),'y:',bool('se' in y))