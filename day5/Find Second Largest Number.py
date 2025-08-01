mylist=[]
for i in range(6):
    user=int(input("Enter the Number:"))
    mylist.append(user)
    mylist.sort()
print(f"the first largest Number is the : {mylist[5]}, \nThe second largest Number is the : {mylist[4]}.")