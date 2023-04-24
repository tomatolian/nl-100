with open('popular-names.txt','r') as f0:
    lis=f0.readlines()
col1=list(map(lambda x:x.split('\t')[0],lis))
dic={}
for i in col1:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1
print(*sorted(dic.items(),key=lambda x: x[1],reverse=True),sep='\n')

#cut -f 1 popular-names.txt |uniq -c |sort