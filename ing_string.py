string = input("Enter String : ")
if string.endswith('ing'):
    string=string+'ly'
else:
    string=string+'ing'
print("Modified string is : ",string)