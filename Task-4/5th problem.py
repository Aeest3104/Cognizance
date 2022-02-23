
space = 4
lines=5
for i in range(0, lines):
        for j in range(0, space):
            print(end=" ")
        space=space-1
        for j in range(0, i+1):
         print("* ", end="")
        print("\r")
 
