input=open('input.txt', 'r')
line = input.read()
line = line.replace('.',' ')
line = line.replace(',',' ')
line = line.replace('?',' ')
line = line.replace('!',' ')
line = line.split()
N= dict()
for x in line:
	x = x.lower()
for i in line:
	if i not in line:
		N[x] = line.count(i)
maxinN=0
for key in N:
	print(key, N[key])
for key in N:
	if N[key] > maxinN:
		maxinN = N[key]
		maxofkey = key
	print(maxinN, maxofkey)
