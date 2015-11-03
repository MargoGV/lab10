enru=open('en-ru.txt', 'r')
A=enru.read()
A=A.split()
B=[]
C=[]
i=0
while i<=len(A)-3:
	B.append(A[i])
	i+=3
j=2
while j<=len(A)-3:
	C.append(A[j])
	j+=3
E = dict(zip(B,C))

input=open('input.txt','r')
N=N.append()
print(E, D, 
