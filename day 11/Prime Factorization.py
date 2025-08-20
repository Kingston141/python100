user = int(input("Enter a number: "))

for i in range(2, user + 1):
    if user % i == 0:   # check if i is a factor
        # check if i is prime
        is_prime = True
        print(f"factors:{i}")
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, "is a prime factor")
