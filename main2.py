from tkinter import *
from tkinter import ttk
from functions import *
import math

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def dropdownConnect(value):
    shapeDropdown.set_menu(*shapeOptions.get(value))


def changeHeader(value):
    global shape
    shape = value
    shapeNamePlaceHolder.set(value)
    if(value == "Square"):
        squareFrame.pack(side="top", fill="both")
        squareLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        squareInputbox.pack(side="left", pady=(10, 10), padx=(10, 0))
        squareMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        squareButtonsFrame.pack(side="top", fill="both")
        squareCalculateButton.pack(
            side="left", pady=(50, 0), padx=(150, 0))
        squareResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        squareFrame.pack_forget()
        squareInputbox.pack_forget()
        squareLabel.pack_forget()
        squareMetricDropdown.pack_forget()
        squareButtonsFrame.pack_forget()
        squareCalculateButton.pack_forget()
        squareResetButton.pack_forget()


def resetButton():
    squareInputbox.delete(0, END)
    squareResultLabel.config(text=" ")


def squareArea():
    if(shape == "Square"):
        if(squareInputbox.get().isdigit()):
            input = int(squareInputbox.get())
            squareArea = input * input
            squareResultLabel.config(
                text=f"Area = {input} x {input} = {squareArea}")
            squareResultFrame.pack(side="top", fill="both")
            squareResultLabel.pack(side="top", pady=(50, 0))
        else:
            return


root = Tk()
root.geometry("600x600")
root.title(" ")
root.configure(bg="#272934")

# Header for the page
# Frame
headerFrame = Frame(root, bg="#272934")
headerFrame.pack(side="top", fill="both")
# Label
headerLabel = ttk.Label(headerFrame, text="Volume and Area Calculator", font=(
    "Ariel", 18, "bold"), background="#272934", foreground="white")
headerLabel.pack(side="top", pady=10)

# Dimension and Shape chooser
chooserFrame = Frame(root, bg="#272934")
chooserFrame.pack(side="top", fill="both")

# Label
dimensionLabel = ttk.Label(chooserFrame, text="Dimension:", font=(
    "Calibri", 14), background="#272934", foreground="white")
dimensionLabel.pack(side="left", padx=(80, 0), pady=(40, 0))
# Dropdown configurations
dimensionOptions = ["Select", "2D", "3D"]
dimensionPlaceholder = StringVar()
dimensionPlaceholder.set(dimensionOptions[0])
# Dropdown Menu
dimensionDropdown = ttk.OptionMenu(
    chooserFrame, dimensionPlaceholder, *dimensionOptions, command=dropdownConnect)
dimensionDropdown.pack(side="left", padx=(10, 0), pady=(40, 0))

# Dropdown Configurations
shapeOptions = {
    "2D": ["Select", "Square", "Rectangle",
           "Triangle", "Circle", "Semi-Circle",
           "Sector", "Ellipse", "Trapezoid",
           "Pentagon", "Hexagon", "Octagon"],
    "3D": ["Select", "Cube", "Cuboid", "Cone", "Cylinder",
           "Sphere", "Hemisphere", "Tetrahedron", "Pyramid"]
}
shapePlaceholder = StringVar()

shapeDropdown = ttk.OptionMenu(
    chooserFrame, shapePlaceholder, "Select", command=lambda value: changeHeader(value))
shapeDropdown.pack(side="right", padx=(0, 80), pady=(40, 0))
# Label
shapeLabel = ttk.Label(chooserFrame, text="Shape:", font=(
    "Calibri", 14), background="#272934", foreground="white")
shapeLabel.pack(side="right", padx=(0, 10), pady=(40, 0))

# Shape Name
shapeNameFrame = Frame(root, bg="#272934")
shapeNameFrame.pack(side="top", fill="both")

shapeNamePlaceHolder = StringVar()

shapeNameLabel = ttk.Label(shapeNameFrame, textvariable=shapeNamePlaceHolder, font=(
    "Calibri", 16, "bold"), background="#272934", foreground="white")
shapeNameLabel.pack(side="top", pady=20)

# Square
squareFrame = Frame(root, bg="#272934")
squareLabel = ttk.Label(squareFrame, text="Edge Length:", font=(
    "Calibri", 14), background="#272934", foreground="white")
squareInputbox = Entry(squareFrame, width=8)
squareMetricOptions = ["cm", "inch", "feet", "cm", "m"]
squareMetricPlaceholder = StringVar()
squareMetricPlaceholder.set(squareMetricOptions[0])

squareMetricDropdown = ttk.OptionMenu(
    squareFrame, squareMetricPlaceholder, *squareMetricOptions)

squareButtonsFrame = Frame(root, bg="#272934")
squareCalculateButton = ttk.Button(
    squareButtonsFrame, text="Calculate", command=squareArea)
squareResetButton = ttk.Button(
    squareButtonsFrame, text="Reset", command=resetButton)
squareResultFrame = Frame(root, bg="#272934")
squareResultLabel = ttk.Label(squareResultFrame, text="Area =", font=(
    "Calibri", 14), background="#272934", foreground="white")
root.mainloop()
