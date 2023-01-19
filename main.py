from tkinter import *
from tkinter import ttk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def menu_func(value):
    shapeMenu.set_menu(*shapeOptions.get(value))


root = Tk()
root.geometry("500x500")
root.title("Area and Volume Calculator")

# Header
headerFrame = Frame(root, bg="#272934")
headerFrame.pack(side="top", fill="both")
headerLabel = ttk.Label(headerFrame, text="Volume and Area Calculator", font=(
    "Calibri", 18, "bold"), background="#272934", foreground="white")
headerLabel.pack(side="top", pady=30)

# Dimension
dimensionFrame = Frame(root, bg="#272934")
dimensionFrame.pack(side="top", fill="both")

dimensionLabel = ttk.Label(dimensionFrame, text="Dimension", font=(
    "Calibri", 14), background="#272934", foreground="white")
dimensionLabel.pack(side="left", pady=25, padx=20)

dimensionOptions = ["Select", "2D", "3D"]
dimensionOption = StringVar()
dimensionOption.set(dimensionOptions[0])

dimensionMenu = ttk.OptionMenu(
    dimensionFrame, dimensionOption, *dimensionOptions, command=menu_func)
dimensionMenu.pack(side="right", pady=25, padx=20)

# Shape
shapeFrame = Frame(root, bg="#272934")
shapeFrame.pack(side="top", fill="both")

shapeLabel = ttk.Label(shapeFrame, text="Area of", font=(
    "Calibri", 14), background="#272934", foreground="white")
shapeLabel.pack(side="left", pady=10, padx=20)

shapeOptions = {
    "2D": ["Select", "Square", "Rectangle",
           "Triangle", "Circle", "Semi-Circle",
           "Sector", "Ellipse", "Trapezoid",
           "Pentagon", "Hexagon", "Octagon"],
    "3D": ["Select", "Cube", "Cuboid", "Cone", "Cylinder",
           "Sphere", "Hemisphere", "Tetrahedron", "Pyramid"]
}
shapeOption = StringVar()

shapeMenu = ttk.OptionMenu(shapeFrame, shapeOption, "Select Dimension")
shapeMenu.pack(side="right", pady=10, padx=20)

# Square

squareFrame = Frame(root, bg="#272934")
squareFrame.pack(side="top", fill="both")

squareLabel = ttk.Label(
    squareFrame, text="Please select the input scale", font=(""))


root.mainloop()
