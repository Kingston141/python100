count=int(input("Enter the Number:"))

list=[]
list2=[]
for i in range(count):
    user=int(input("Enter the numbers:"))
    list.append(user)
print(list)
for j in range(len(list) -1,-1,-1):
    list2.append(list[j])
print(list2)