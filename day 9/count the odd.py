user=int(input("Enter a number: "))
odd = []

for i in range(1,user+1):
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        odd.append(i)
        print(i, "is an odd number")
print("Odd numbers up to", user, "are:", odd)
print("Total odd numbers up to", user, "are:", len(odd))
