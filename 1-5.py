def ngram(N,w):
  ans=[]
  lis=w.split(' ')
  for i in range(len(lis)-1):
    ans.append(lis[i:i+N])
  return ans

print(ngram(2,'I am an NLPer'))