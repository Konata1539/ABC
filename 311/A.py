lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

a = 0
b = 0
c = 0

for i in range(0,len(lines[1])):
    if lines[1][i] == "A":
        a = a + 1
    elif lines[1][i] == "B":
        b = b + 1
    elif lines[1][i] == "C":
        c = c + 1
    if a>=1 and b>=1 and c>=1:
        print(i+1)
        break

    
