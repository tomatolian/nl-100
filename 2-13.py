f=open('col1.txt','r')
f1=open('col2.txt','r')
f2=open('merge_col.txt','w')
print(*map(lambda x: x[0].strip()+'\t'+x[1].strip(),zip(f.readlines(),f1.readlines())),sep='\n',file=f2)
f.close()
f1.close()
f2.close()