n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()

n=9
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j,end=" "))
    print()

max(1,2,3,4)
n=int(input("n: "))
for i in range(n):
    for j in range(n):
        print(
            max(max(i+1,j+1),max(n-j,n-i)),end=" "
        )
        print()