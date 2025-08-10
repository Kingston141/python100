user = int(input("Enter a number to check if it's an Armstrong number: "))

original = user


num_digits = len(str(user))

result = 0
temp = user
while temp > 0:
    digit = temp % 10
    result += digit ** num_digits
    temp //= 10

if result == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is NOT an Armstrong number.")
