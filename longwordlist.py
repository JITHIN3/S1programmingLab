n= int(input("Enter The No of items : "))
list =[]
for i in range(n):
    x = input("Enter item : \n")
    list.append(x)
print(list)
max = len(list[0])
temp = list[0]
for i in list:
    if len(i)>max:
        max = len(i)
        temp = i
print("The word having logest lenth is ",temp,"length is : ",max )