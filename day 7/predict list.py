n=int(input("Enter the number of elements in it :"))
mylist=[]
for i in range(n):
    user=int(input("Enter the numbers in which has entered into list:"))
    mylist.append(user)
print(mylist)

for i in mylist:
    positive_count=0
    negative_count=0
    zero_count=0
    if i==0:
        zero_count+=1
        print("Zero is present in the list:",zero_count)
    elif i>0:
        positive_count+=1
        print("Zero is present in the list:",positive_count)
    else:
        negative_count+=1
        print("Zero is present in the list:",zero_count)
    
