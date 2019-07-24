def is_prime(num):
    is_pri=True
    if num<2:
        return False
    else:
        for i in range(2,(num//2)+1):
            if num%i==0:
                return False
    return True
    


num1=int(input("Enter the Lower bound"))
num2=int(input("Enter the upper bound"))
print("Prime numbers are:")
for i in range(num1,num2+1):
    temp=is_prime(i)
    if temp:
        print(i)
    else:
        continue
