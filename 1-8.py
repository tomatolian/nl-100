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

print(cipher('aiueoAIUEO123'))