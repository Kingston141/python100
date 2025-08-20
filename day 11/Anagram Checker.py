String1 = input("Enter the first word: ").lower().replace(" ", "")
String2 = input("Enter the second word: ").lower().replace(" ", "")

if sorted(String1) == sorted(String2):
    print("It's an anagram ✅")
else:
    print("It's not an anagram ❌")
