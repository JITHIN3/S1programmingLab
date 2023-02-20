n = int(input("Enter the limit :"))
list = []
a = 0
for i in range(n):
    x = input("Enter The name : ")
    list.append(x)
    for i in list:
        for j in i:
            if 'a' in j:
                a = a + 1
print("The Occcurence of a is : ", a)
