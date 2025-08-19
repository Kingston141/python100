user=int(input("Enter the number that has limit"))
mylist=[]
a,b=0,1
for i in range(user):
    mylist.append(a)
    a,b=b,a+b
print(mylist)