color1=["red","blue","yellow"]
color2 =["green","blue","pink"]
print(color1)
print(color2)
for i in range(len(color1)):
    if color1[i]not in color2:
        print("The Color is : ",color1[i])

