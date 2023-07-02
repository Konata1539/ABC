import sys

input_lines = []
for line in sys.stdin:
    input_lines.append(line.strip())

a, b, c, d = input_lines[:4]

l = a.split(" ")
x = b.split(" ")
y = c.split(" ")
z = d.split(" ")

k = 0

for i in range(0,len(x)):
    p = 0
    for j in range(0,len(y)):
        if x[i] == y[j]:
            k = k + int(z[j + 1])
            p = p + 1
        if j == len(y) - 1 and  p == 0:
            k = k + int(z[0])

print(k)
