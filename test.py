import math


def square(side):
    area = side * side


def rectangle(length, breadth):
    area = length * breadth


def triangleBaseHeight(base, height):
    area = 0.5 * (base * height)


def triangleSides(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5


def triangle2SidesAngle(side1, side2, angle):
    area = (1 / 2) * side1 * side2 * math.sin(angle)


def triangle2AnglesSide(angle1, angle2, side):
    area = (1 / 2) * side * side * math.sin(angle1) * math.sin(angle2) / math.sin(angle1 + angle2)


def circle(radius):
    area = 3.14 * (radius * radius)


def semicircle(radius):
    area = 0.5 * 3.14 * (radius * radius)


def sector(radius, angle):
    area = 3.14 * radius * radius * angle / 360


def ellipse(minor, major):
    area = 3.14 * minor * major


def trapezoid(base1, base2, height):
    area = (base1 + base2) / 2 * height


def parallelogram(base, height):
    area = base * height


def rhombus(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2


def pentagon(side):
    area = (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * side * side) / 4


def hexagon(side):
    area = ((3 * math.sqrt(3) * (side * side)) / 2)


def octagon(side):
    area = (2 * (1 + (math.sqrt(2))) * side * side)


import math


def cube(side):
	area = 6 * side ** 2
	

def cuboid(length, breadth, height):
	area = 2 * (length * breadth + breadth * height + length * height)
	

def cone(radius, height):
	area = 3.14 * radius(radius + math.sqrt((height ** 2) + (radius ** 2))
			     

def cylinder(radius, height):
	area = 2 * 3.14 * radius * height + 2 * 3.14 * (radius ** 2)
			     

def sphere(radius):
	area = 4 * 3.14 * (radius ** 2)
			     

def hemisphere(radius):
	area = 2 * 3.14 * (radius **2)
			     

def tetrahedron(side):
	area = math.sqrt(3) * (side ** 2)
			     

def pyramid(length, width, heigth):
	area = length * width + length * math.sqrt((width/2)**2 + height**2) + width * math.sqrt((length/2)**2 + height ** 2)


import math

def cube(side):
	volume = side **3

def cuboid(length, breadth, height):
	volume = length * breadth * height

def cone(radius, height):
	volume = 0.333 * 3.14 * (radius ** 2) * height

def cylinder(radius, height):
	volume = 3.14 * (radius ** 2) * height

def sphere(radius):
	volume = 1.333 * 3.14 * (radius ** 3)

def hemisphere(radius):
	volume = 0.6667 * 3.14 * (radius ** 3)

def tetrahedron(side):
	volume = (side ** 3) / 6 * math.sqrt(2)

def pyramid(length, width, height):
	volume = (length * width * height) / 3
