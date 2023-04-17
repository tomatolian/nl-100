import re

def cipher(w):
  ans=''
  for i in w:
    flag=re.match('[a-z]',i)
    if flag:
      ans+=chr(219-ord(i))
    else:
      ans+=i
  return ans

res=cipher('aiueoAIUEO123')
print('encode:',res)
res1=cipher(res)
print('decode:',res1)