num=int(input("Enter the number"))
sum=0
for i in range(2,num+1):
    sum=sum+(1/(i*i*i))
print("Sum of series is",sum)