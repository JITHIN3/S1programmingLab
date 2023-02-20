n = int(input("Enter The limit : "))
list =[]
for x in range(n):
    x = int(input("Enter The No : \n"))
    if x > 100:
        list.append(x)
    else:
        list.append('over')
print(list)
