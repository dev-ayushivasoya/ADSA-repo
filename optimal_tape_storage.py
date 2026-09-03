n=int(input("Enter no.of files:"))
length=[]
print("Enter the length of files:")
for i in range (n):
    length.append(int(input()))

for i in range (n-1):
    min_index=i
    for j in range (i+1,n):
        if length[j]<length[min_index]:
            min_index=j
    temp=length[i]
    length[i]=length[min_index]
    length[min_index]=temp
print("Optimal order:",end=" ")
for i in range (n):
    print(length[i],end=" ")

total=0
current=0
for i in range(n):
    current=current+length[i]
    total=total+current
print("\nTotal retrieval time:",total)
