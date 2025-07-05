
import calculate

lenght = float(input("Enter the lenght of the rectangle: "))
width = float(input("Enter the width of the ectangle: "))

area = calculate.area(lenght, width)
perimeter = calculate.perimeter(lenght, width)


print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")