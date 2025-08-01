def factorial(num):
    if num==0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
user=int(input("ENter a number to find the factorial:"))
print(f"the factorial of {user}: {factorial(user)}")