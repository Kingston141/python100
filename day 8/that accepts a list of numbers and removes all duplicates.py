user=int(input("Enter a Count of number: "))

list1=[]
list2=[]
for i in range(user):
    e=int(input("Enter the Number that has to list append :"))
    list1.append(e)
print(f"The value of user inserted in the list :{list1}")
list1=list(set(list1))
for j in list1:
    list2.append(j)
print(f"The after Removed the duplicates :{list2}")
    

    
