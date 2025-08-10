n = 5
mylist = []
vowel = 'aeiouAEIOU'
count = 0  # ✅ Move count outside the loop

for i in range(n):
    user = input("Enter the word: ")
    mylist.append(user)

    if user and user[0] in vowel:
        print("It starts with a vowel.")
        count += 1  # ✅ Increment the count
    else:
        print("It does not start with a vowel.")

print(f"\nWords entered: {mylist}")
print(f"Total words starting with a vowel: {count}")
