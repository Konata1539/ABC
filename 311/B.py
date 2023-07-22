lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

people, day = map(int, lines[0].split())
list = []
for i in range(0,day):
    count = 0
    for j in range(1,people+1):
        if lines[j][i] == "o":
            count += 1
        if count == people:
            list.append(i)

count = 0
t = 0
if len(list) == 1:
    t = 1
for i in range(0,len(list)-1):
    if list[i] + 1 == list[i+1]:
        count += 1
        if i == len(list)-2 and count >= t:
            t = count+1
    else:
        if count >= t:
            t = count+1
        count = 0
    
print(t)