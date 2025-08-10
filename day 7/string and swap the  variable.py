user = input("Enter the string: ")
if len(user) < 2:
    print("Too short to swap.")
else:
    swapped = user[-1] + user[1:-1] + user[0]
    print("After swap:", swapped)
    print("Length:", len(user))
