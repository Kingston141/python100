user = input("Enter a string: ").lower()
frequency = {}

for char in user:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for char, count in frequency.items():
    print(f"{char} : {count}")
