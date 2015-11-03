A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
G = (A.difference(B)).intersection(C.difference(D))
E = (D.difference(A)).intersection(B.difference(C))
N = G.union(E)
print(N)

