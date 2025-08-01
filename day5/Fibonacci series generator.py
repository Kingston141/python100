n = int(input("Enter how many terms you want: "))

# Starting two numbers of the series
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))   


# Optional: store in a list
fibonacci = []

# Loop n times
for i in range(n):
    fibonacci.append(a)
    next_num = a + b
    a = b
    b = next_num

print("The Fibonacci series is:", fibonacci)
