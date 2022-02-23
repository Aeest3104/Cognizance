string=str(input("Enter a string:"))
i=len(string)
for j in range(0,i,1):
  if(j%2==0):
   print(string[j])
  else:
   print()
   