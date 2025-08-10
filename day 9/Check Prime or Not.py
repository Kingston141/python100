def is_prime():
    user=int(input("Enter the number: "))
    list=[]
    for i in range(2,user+1):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            list.append(i)
                
    print("Prime numbers between 1 and", user, "are:")
    print(list)
is_prime()
            
        
