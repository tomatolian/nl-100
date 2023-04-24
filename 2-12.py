with open('popular-names.txt','r') as f0:
    lis=f0.readlines()
f=open('col1.txt','w')
f1=open('col2.txt','w')
col1=list(map(lambda x:x.split('\t')[0],lis))
col2=list(map(lambda x:x.split('\t')[1],lis))
print(*col1,sep='\n',file=f)
print(*col2,sep='\n',file=f1)
f.close()
f1.close()
#cut -f 1 popular-names.txt
#cut -f 2 popular-names.txt