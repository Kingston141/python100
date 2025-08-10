list=[2,4,6,1,134]

for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
        flag=False
        break
    else:
        flag=True
if flag:
    print("List is sorted")
else:
    print("list is not sorted")