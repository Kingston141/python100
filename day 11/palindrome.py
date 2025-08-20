num = input("Enter the number: ")   # keep it as string directly
if num == num[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")