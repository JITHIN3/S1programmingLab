string = input("Enter the string : ")

count = 0
for i in range(len(string)):
    if(string[i]!=""):
        count=count+1
print("Count of strng is : ",count)