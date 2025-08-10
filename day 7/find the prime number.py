n = int(input("Enter the number (find primes from 1 to n): "))
prime_list = []

for num in range(2, n + 1):  # 1 is not prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Efficient check
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(num)

print("Prime numbers between 1 and", n, "are:")
print(prime_list)
