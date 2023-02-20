"""list =[-20,40,-56,67,-8,9,78]
print("The List is : ",list)
newlist =[ x for x in list if x>=0]
print("Postive Numbers are in List : ",newlist)

n = int(input("Enter the number : "))
list =[]
for x in range(n):
    a = int(input("Enter numbers :"))
    list.append(a)
print(list)
list2=[x**2 for x in list]
print(list2)"""
"""word = input("Enter Word : ")
vowels = [x for x in word if x in ["a","e","i","o","u"]]
print("The vowels in the word : ",vowels)"""
w = input("enter a word: ")
ord = [ord(x) for x in w]
print("the ordinal value is: ", ord)
