def revnum(num):
    rev=0
    while True:
        if num==0:
            break
        temp=num%10
        num=num//10
        rev=rev*10+temp
    return rev





num=int(input("Enter the number"))
rever=revnum(num)

print(f"The Reverse is {rever}")