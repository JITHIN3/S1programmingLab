a = int(input("Enter The Current Year : \n"))
f = int(input("Enter Final Year : \n"))
print ("Future Leap Years are : \n")
for x in range(a,f+1):
    if(x%4==0 and x %100 !=0 or x%400==0):
        print(x)