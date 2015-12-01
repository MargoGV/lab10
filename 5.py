input=open('input.txt','r')
output=open('ru-en.txt','w')
s=input.read()
sl={}
while len(s)>1:
  sl[s[:s.index(' - ')]]=s[s.index( - )+3:s.index('\n')]
  s=s[s.index('\n')+1:]
v=[sl[x]+' - ' +x for x in sl]
v=sorted(v)
for r in range (len(sl)):
  print(v[r],file=output)
