A = input()
l = A.split(" ") 
l[0] = int(l[0])
l[1] = int(l[1])
if abs(l[0] - l[1]) == 1:
    if l[0] == 2 or l[0] == 5 or l[0] == 8:
        print("Yes")
    elif l[1] == 2 or l[1] == 5 or l[1] == 8:
        print("Yes")
    else:   
        print("No")
else:
    print("No")
