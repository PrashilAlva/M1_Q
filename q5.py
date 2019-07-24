print("Fibonnaci Series upto 34 is")
old=0
new=1
print(old,new,end=' ')
while True:
    if new==34:
        break
    temp=old+new
    print(temp,end=' ')
    old=new 
    new=temp