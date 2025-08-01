user=input("Enter a word or phrase: ").lower().replace(" ", "")

if user==user[::-1]:
    print("The word or phrase is a plaindrome:")
else:
    print("its not the palindrome")