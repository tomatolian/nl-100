import random

t="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
lis=[i[0]+''.join(random.sample(i[1:-1],len(i[1:-1])))+i[-1] if len(i)>4 else i for i in t.split()]
print(lis)
