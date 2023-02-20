list1 =[1,6,7,9,3,4]
list2 =[2,6,39,57,89,45,67]
print("Elements of List1 : ",list1)
print("Elements of List2 : ",list2)
if(len(list1) == len(list2)):
    print("Length is same")
else:print("Length is different")
s1 =0
s2 =0
for i in range(len(list1)):
    s1 =s1+list1[i]
    print("Sum of listi is : ",s1)
for i in range(len(list2)):
    s2 = s2+list2[i]
    print("Sum of list2 is : ",s2)
if(s1==s2):
    print("sum is equal")
else:
    print("Sum is different")
print("Common element : ")
for i in list1:
    for j in list2:
        if i==j:
            print(i)