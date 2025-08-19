user=input("Enter the Sentence:")
user=user.split()
freq={}

for i in user:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(f"frequency Word:",freq)