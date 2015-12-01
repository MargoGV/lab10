input=open('input.txt','r')
s=input.read()
s=s.replace('.',' ')
s=s.replace(',',' ')
s=s.replace('?',' ')
s=s.replace('!',' ')
s=s.replace('\n',' ')
s=s.lower()
st={}
while s[0]==' ':
  s=s[1:]
s=s+' '
while len(s)>0:
  l=s[0:s.index(' ')]
  plent(l)
  if l in st:
    st[l]+=1
  else:
    st[l]=1
  s=s[s.index(' ")+1:]
while s[len(s)-1]==' ':
  s=[:len(s)-1]
print(len(st))
max=0
maX=''
for key in st:
  if st[key]>=max:
    maX=key
    max=st[key]
print(maX,st[maX])

