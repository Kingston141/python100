user=input("Enter the string:")
vowels='aeiou'
for i in user:
    if i in vowels:
        print("*",end='')
    else:
        print(i,end='')
        
