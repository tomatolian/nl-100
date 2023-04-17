t='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
dic=dict([(i[0],ind+1) if (ind+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]) else (i[0:2],ind+1)  for ind,i in enumerate(t.split(' '))])
print(dic)