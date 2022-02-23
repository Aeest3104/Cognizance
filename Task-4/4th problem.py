num=int(input("Enter number:"))
a=num
r=0
while(num>0):
    dig=num%10
    r=r*10+dig
    num=num//10
if(a==r):
    print("True")
else:
    print("False")
