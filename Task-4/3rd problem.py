from tabulate import tabulate
l1=[["Roll No","Name","Marks"]]
dup=1
condition='yes'
while (condition.lower()=='yes'):
    print("Enter Add to Add A Row\nEnter Table to Display The Table\nEnter Element to Display A single Row")
    choice=str(input("Enter Your Choice:"))
    if choice=='Add':
        l1.append([int(input("Enter The Roll No.:")),input("Enter The Student Name:"),int(input("Enter The Marks:"))])
    elif choice=='Table':
        print(tabulate(l1,headers='firstrow',tablefmt='grid'))
    elif choice=='Element':
        ele = input("Enter The  Name of the student:")
        for i in range(len(l1)):
             l=[]
             if ele==l1[i][1]:
                l=[l1[i]]
                print(l)
                print(tabulate(l,headers=["Roll No","Name","Marks"],tablefmt='grid'))
                
        if l==[]:
            print("No Data Found")
    else:
        print("Invalid try again\n")
    condition=input("Do You Want To make some more changes? (Yes/No):\n")
