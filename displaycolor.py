color = int(input("Enter The No of Colors : "))
listcolor =[]
for i in range(color):
    a =input("Enter The Color : ")
    listcolor.append(a)
print(listcolor)
print("The First Color is : ",listcolor[0])
print("The last Color is  : ",listcolor[-1])