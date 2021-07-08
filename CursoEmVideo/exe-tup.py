tuplaz = 'primeira', 'segunda', 'terceira'
for pos, numero in enumerate(tuplaz):
    print(pos, numero)

for pos in enumerate(tuplaz):
    print(pos)

a = (2, 5, 7)
b = (1, 3, 7, 10)
c = a + b
print(len(c))
print(c.count(7))
print(sorted(c))
print(c.index(7, 3))

