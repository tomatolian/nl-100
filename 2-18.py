with open('popular-names.txt','r') as f:
    print(*sorted(f.readlines(),key=lambda x : x.split('\t')[2],reverse=True))