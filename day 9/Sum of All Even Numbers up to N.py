user=int(input("Enter the range number that has to find the even number:"))
even=[]
odd=[]
for i in range(1,user+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
add=0
for j in even:
    add+=j
    print(j)
print("Sum of all even numbers up to", user, "is:", add)