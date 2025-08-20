user = input("Enter the sentence: ")
j = user.split()

for i in j:
    print(i[0].upper() + i[1:], end=" ")
