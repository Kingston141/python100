user=int(input("Enter a number: "))

for i in range(1,user+1):
    for j in range(1,i+1):
        print((j+1)%2 ,end=' ')
    print()
