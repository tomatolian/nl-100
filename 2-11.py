file='popular-names.txt'

with open(file) as f:
    lis=[i.replace('\t',' ')for i in f]

with open('tmp.txt','w') as f1:
    print(*lis,file=f1,sep='')
#cat popular-names.txt|tr '\t' ' '>tmp1.txt 