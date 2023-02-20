class Rectangel:
    def __int__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def perimeter(self):
        return (2 * (self.length + self.breadth))


l1 = int(input("Enter legth 1: "))
b1 = int(input("Enter bredth 1 : "))
r1 = Rectangel(l1, b1)
print("Area of Rectngl1 : ", r1.area())
print("Perimeter of rec1 : ", r1.perimeter())
l2 = int(input("Enter legth2 : "))
b2 = int(input("Enter bredth2 : "))
r2 = Rectangel(l2, b2)
print("Area of Rectangle2 : ", r2.area())
print("Perimeter of rec2 : ", r2.perimeter())
a1 = r1.area()
a2 = r2.area()
if a1 > a2:
    print("Area of rec 1 is high")
elif a1 == a2:
    print("Area is same")
else:
    print("Area of rec2 is high")
