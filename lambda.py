#Area of Square
a =int(input("Enter The side of Square : "))
s_area = lambda a:a*a
print("Area of Square : ",s_area(a))
#Area of Rectangel
l =int(input("Enter Length of Rectangle : "))
b =int(input("Enter Breadth of Rectangel : "))
r_area = lambda  l,b:l*b
print("Area of Recangle : ",r_area(l,b))
#Area of Triangle
b =int(input("Enter The Base of Triangle : "))
h =int(input("Enter The Height of Triangle : "))
t_area =lambda b,h:5*b*h
print("Area of a Triangle",t_area(b, h))
