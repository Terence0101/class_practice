m = input()
a = input()
b = []

for i in range (len(m)):
    if m[i] == a.upper() or m[i] == a.lower():
        b.append(i)

for j in range (len(b)-1):
    print(b[j+1]-b[j], end=' ')
