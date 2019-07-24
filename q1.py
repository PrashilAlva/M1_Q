#To check a no is prime or not

num=int(input("Enter the no?"))
is_prime=True
if num<2:
    is_prime=False
else:
    for i in range(2,(num//2+1)):
        if num%i==0:
            is_prime=False

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")
