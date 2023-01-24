from tkinter import *
from tkinter import ttk
from functions import *
import math

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

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
# Function, binds the dimension dropdown and the shape dropdown


def dropdownConnect(value):
    shapeDropdown.set_menu(*shapeOptions.get(value))


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

# Function for changing the shape name

answer = "String"
isClicked = False


def changeHeader(value):
    global answer
    answer = value
    shapeNamePlaceHolder.set(value)
    if(value == "Square" or value == "Pentagon" or value == "Hexagon" or value == "Octagon" or value == "Cube" or value == "Tetrahedron"):
        sideFrame.pack(side="top", fill="both")
        sideLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        sideInputbox.pack(side="left", pady=(10, 10), padx=(10, 0))
        sideMetricDropdown.pack(side="right", pady=(10, 10), padx=(0, 170))
        sideButtonsFrame.pack(side="top", fill="both")
        sideCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        sideResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        sideFrame.pack_forget()
        sideInputbox.pack_forget()
        sideLabel.pack_forget()
        sideMetricDropdown.pack_forget()
        sideButtonsFrame.pack_forget()
        sideCalculateButton.pack_forget()
        sideResetButton.pack_forget()

    if(value == "Rectangle"):
        rectangleLengthFrame.pack(side="top", fill="both")
        rectangleLengthLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        rectangleLengthInputbox.pack(side="left", pady=(10, 10), padx=(58, 0))
        rectangleLengthMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        rectangleWidthFrame.pack(side="top", fill="both")
        rectangleWidthLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        rectangleWidthInputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        rectangleWidthMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        rectangleButtonsFrame.pack(side="top", fill="both")
        rectangleCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        rectangleResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        rectangleLengthFrame.pack_forget()
        rectangleLengthLabel.pack_forget()
        rectangleLengthInputbox.pack_forget()
        rectangleLengthMetricDropdown.pack_forget()
        rectangleWidthFrame.pack_forget()
        rectangleWidthLabel.pack_forget()
        rectangleWidthInputbox.pack_forget()
        rectangleWidthMetricDropdown.pack_forget()
        rectangleButtonsFrame.pack_forget()
        rectangleCalculateButton.pack_forget()
        rectangleResetButton.pack_forget()

    if(value == "Triangle"):
        triangleEdge1Frame.pack(side="top", fill="both")
        triangleEdge1Label.pack(side="left", pady=(10, 0), padx=(150, 0))
        triangleEdge1Inputbox.pack(side="left", pady=(10, 10), padx=(63, 0))
        triangleEdge1MetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        triangleEdge2Frame.pack(side="top", fill="both")
        triangleEdge2Label.pack(side="left", pady=(10, 0), padx=(150, 0))
        triangleEdge2Inputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        triangleEdge2MetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        triangleEdge3Frame.pack(side="top", fill="both")
        triangleEdge3Label.pack(side="left", pady=(10, 0), padx=(150, 0))
        triangleEdge3Inputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        triangleEdge3MetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        triangleButtonsFrame.pack(side="top", fill="both")
        triangleCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        triangleResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        triangleEdge1Frame.pack_forget()
        triangleEdge1Label.pack_forget()
        triangleEdge1Inputbox.pack_forget()
        triangleEdge1MetricDropdown.pack_forget()
        triangleEdge2Frame.pack_forget()
        triangleEdge2Label.pack_forget()
        triangleEdge2Inputbox.pack_forget()
        triangleEdge2MetricDropdown.pack_forget()
        triangleEdge3Frame.pack_forget()
        triangleEdge3Label.pack_forget()
        triangleEdge3Inputbox.pack_forget()
        triangleEdge3MetricDropdown.pack_forget()
        triangleButtonsFrame.pack_forget()
        triangleCalculateButton.pack_forget()
        triangleResetButton.pack_forget()

    if(value == "Circle" or value == "Semi-Circle" or value == "Sphere" or value == "Hemisphere"):
        radiusFrame.pack(side="top", fill="both")
        radiusLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        radiusInputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        radiusMetricDropdown.pack(side="right", pady=(10, 10), padx=(0, 170))
        circleButtonsFrame.pack(side="top", fill="both")
        circleCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        circleResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        radiusFrame.pack_forget()
        radiusLabel.pack_forget()
        radiusInputbox.pack_forget()
        radiusMetricDropdown.pack_forget()
        circleButtonsFrame.pack_forget()
        circleCalculateButton.pack_forget()
        circleResetButton.pack_forget()

    if(value == "Sector"):
        sectorRadiusFrame.pack(side="top", fill="both")
        sectorRadiusLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        sectorRadiusInputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        sectorRadiusMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        sectorAngleFrame.pack(side="top", fill="both")
        sectorAngleLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        sectorAngleInputbox.pack(side="left", pady=(10, 10), padx=(74, 0))
        sectorAngleMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        sectorButtonsFrame.pack(side="top", fill="both")
        sectorCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        sectorResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        sectorRadiusFrame.pack_forget()
        sectorRadiusLabel.pack_forget()
        sectorRadiusInputbox.pack_forget()
        sectorRadiusMetricDropdown.pack_forget()
        sectorAngleFrame.pack_forget()
        sectorAngleLabel.pack_forget()
        sectorAngleInputbox.pack_forget()
        sectorAngleMetricDropdown.pack_forget()
        sectorButtonsFrame.pack_forget()
        sectorCalculateButton.pack_forget()
        sectorResetButton.pack_forget()

    if(value == "Ellipse"):
        majorAxisFrame.pack(side="top", fill="both")
        majorAxisLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        majorAxisInputbox.pack(side="left", pady=(10, 10), padx=(10, 0))
        majorAxisMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 140))
        minorAxisFrame.pack(side="top", fill="both")
        minorAxisLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        minorAxisInputbox.pack(side="left", pady=(10, 10), padx=(10, 0))
        minorAxisMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 140))
        ellipseButtonsFrame.pack(side="top", fill="both")
        ellpiseCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        ellipseResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        majorAxisFrame.pack_forget()
        majorAxisLabel.pack_forget()
        majorAxisInputbox.pack_forget()
        majorAxisMetricDropdown.pack_forget()
        minorAxisFrame.pack_forget()
        minorAxisLabel.pack_forget()
        minorAxisInputbox.pack_forget()
        minorAxisMetricDropdown.pack_forget()
        ellipseButtonsFrame.pack_forget()
        ellpiseCalculateButton.pack_forget()
        ellipseResetButton.pack_forget()

    if(value == "Trapezoid"):
        trapezoidBase1Frame.pack(side="top", fill="both")
        trapezoidBase1Label.pack(side="left", pady=(10, 0), padx=(150, 0))
        trapezoidBase1Inputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        trapezoidBase1MetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        trapezoidBase2Frame.pack(side="top", fill="both")
        trapezoidBase2Label.pack(side="left", pady=(10, 0), padx=(150, 0))
        trapezoidBase2Inputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        trapezoidBase2MetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        trapezoidHeightFrame.pack(side="top", fill="both")
        trapezoidHeightLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        trapezoidHeightInputbox.pack(side="left", pady=(10, 10), padx=(64, 0))
        trapezoidHeightMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        trapezoidButtonsFrame.pack(side="top", fill="both")
        trapezoidCalculateButton.pack(side="left", pady=(50, 0), padx=(150, 0))
        trapezoidResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        trapezoidBase1Frame.pack_forget()
        trapezoidBase1Label.pack_forget()
        trapezoidBase1Inputbox.pack_forget()
        trapezoidBase1MetricDropdown.pack_forget()
        trapezoidBase2Frame.pack_forget()
        trapezoidBase2Label.pack_forget()
        trapezoidBase2Inputbox.pack_forget()
        trapezoidBase2MetricDropdown.pack_forget()
        trapezoidHeightFrame.pack_forget()
        trapezoidHeightLabel.pack_forget()
        trapezoidHeightInputbox.pack_forget()
        trapezoidHeightMetricDropdown.pack_forget()
        trapezoidButtonsFrame.pack_forget()
        trapezoidCalculateButton.pack_forget()
        trapezoidResetButton.pack_forget()

    if(value == "Cuboid" or value == "Pyramid"):
        cuboidPyramidLengthFrame.pack(side="top", fill="both")
        cuboidPyramidLengthLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        cuboidPyramidLengthInputbox.pack(
            side="left", pady=(10, 10), padx=(64, 0))
        cuboidPyramidLengthMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        cuboidPyramidWidthFrame.pack(side="top", fill="both")
        cuboidPyramidWidthLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        cuboidPyramidWidthInputbox.pack(
            side="left", pady=(10, 10), padx=(68, 0))
        cuboidPyramidWidthMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        cuboidPyramidHeightFrame.pack(side="top", fill="both")
        cuboidPyramidHeightLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        cuboidPyramidHeightInputbox.pack(
            side="left", pady=(10, 10), padx=(64, 0))
        cuboidPyramidHeightMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        cuboidPyramidButtonsFrame.pack(side="top", fill="both")
        cuboidPyramidCalculateButton.pack(
            side="left", pady=(50, 0), padx=(150, 0))
        cuboidPyramidResetButton.pack(
            side="right", pady=(50, 0), padx=(0, 170))
    else:
        cuboidPyramidLengthFrame.pack_forget()
        cuboidPyramidLengthLabel.pack_forget()
        cuboidPyramidLengthInputbox.pack_forget()
        cuboidPyramidLengthMetricDropdown.pack_forget()
        cuboidPyramidWidthFrame.pack_forget()
        cuboidPyramidWidthLabel.pack_forget()
        cuboidPyramidWidthInputbox.pack_forget()
        cuboidPyramidWidthMetricDropdown.pack_forget()
        cuboidPyramidHeightFrame.pack_forget()
        cuboidPyramidHeightLabel.pack_forget()
        cuboidPyramidHeightInputbox.pack_forget()
        cuboidPyramidHeightMetricDropdown.pack_forget()
        cuboidPyramidButtonsFrame.pack_forget()
        cuboidPyramidCalculateButton.pack_forget()
        cuboidPyramidResetButton.pack_forget()

    if(value == "Cone" or value == "Cylinder"):
        coneCylinderRadiusFrame.pack(side="top", fill="both")
        coneCylinderRadiusLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        coneCylinderRadiusInputbox.pack(
            side="left", pady=(10, 10), padx=(64, 0))
        coneCylinderRadiusMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        coneCylinderHeightFrame.pack(side="top", fill="both")
        coneCylinderHeightLabel.pack(side="left", pady=(10, 0), padx=(150, 0))
        coneCylinderHeightInputbox.pack(
            side="left", pady=(10, 10), padx=(64, 0))
        coneCylinderHeightMetricDropdown.pack(
            side="right", pady=(10, 10), padx=(0, 170))
        coneCylinderButtonsFrame.pack(side="top", fill="both")
        coneCylinderCalculateButton.pack(
            side="left", pady=(50, 0), padx=(150, 0))
        coneCylinderResetButton.pack(side="right", pady=(50, 0), padx=(0, 170))
    else:
        coneCylinderRadiusFrame.pack_forget()
        coneCylinderRadiusLabel.pack_forget()
        coneCylinderRadiusInputbox.pack_forget()
        coneCylinderRadiusMetricDropdown.pack_forget()
        coneCylinderHeightFrame.pack_forget()
        coneCylinderHeightLabel.pack_forget()
        coneCylinderHeightInputbox.pack_forget()
        coneCylinderHeightMetricDropdown.pack_forget()
        coneCylinderButtonsFrame.pack_forget()
        coneCylinderCalculateButton.pack_forget()
        coneCylinderResetButton.pack_forget()


def reset():
    dimensionDropdown.set_menu(*dimensionOptions)


def sideButton():
    if(answer == "Square"):
        if(sideInputbox.get().isdigit()):
            sideInput = int(sideInputbox.get())
            squareArea = sideInput * sideInput
            squareResultLabel = ttk.Label(resultFrame, text=f"Area = {sideInput} x {sideInput} = {squareArea}", font=(
                "Calibri", 14), background="#272934", foreground="white")
            resultFrame.pack(side="top", fill="both")
            squareResultLabel.pack(side="top", pady=(50, 0))
            sideInputbox.delete(0, END)
            sideInputbox.config(state=DISABLED)
            sideMetricDropdown.config(state=DISABLED)
            sideCalculateButton.config(state=DISABLED)
            shapeDropdown.config(state=DISABLED)
        else:
            return

    # Dropdown Menu
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

# Square, Pentagon, Hexagon, Octagon, Cube,Tetrahedron
sideFrame = Frame(root, bg="#272934")
sideLabel = ttk.Label(sideFrame, text="Edge Length:", font=(
    "Calibri", 14), background="#272934", foreground="white")
sideInputbox = Entry(sideFrame, width=8)
sideMetricOptions = ["cm", "inch", "feet", "cm", "m"]
sideMetricPlaceholder = StringVar()
sideMetricPlaceholder.set(sideMetricOptions[0])

sideMetricDropdown = ttk.OptionMenu(
    sideFrame, sideMetricPlaceholder, *sideMetricOptions)

sideButtonsFrame = Frame(root, bg="#272934")
sideCalculateButton = ttk.Button(
    sideButtonsFrame, text="Calculate", command=sideButton)
sideResetButton = ttk.Button(sideButtonsFrame, text="Reset", command=reset)

# Rectangle
rectangleLengthFrame = Frame(root, bg="#272934")
rectangleLengthLabel = ttk.Label(rectangleLengthFrame, text="Length:", font=(
    "Calibri", 14), background="#272934", foreground="white")
rectangleLengthInputbox = Entry(rectangleLengthFrame, width=8)
rectangleLengthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
rectangleLengthMetricPlaceholder = StringVar()
rectangleLengthMetricPlaceholder.set(rectangleLengthMetricOptions[0])

rectangleLengthMetricDropdown = ttk.OptionMenu(
    rectangleLengthFrame, rectangleLengthMetricPlaceholder, *rectangleLengthMetricOptions)

rectangleWidthFrame = Frame(root, bg="#272934")
rectangleWidthLabel = ttk.Label(rectangleWidthFrame, text="Width:", font=(
    "Calibri", 14), background="#272934", foreground="white")
rectangleWidthInputbox = Entry(rectangleWidthFrame, width=8)
rectangleWidthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
rectangleWidthMetricPlaceholder = StringVar()
rectangleWidthMetricPlaceholder.set(rectangleWidthMetricOptions[0])

rectangleWidthMetricDropdown = ttk.OptionMenu(
    rectangleWidthFrame, rectangleWidthMetricPlaceholder, *rectangleWidthMetricOptions)

rectangleButtonsFrame = Frame(root, bg="#272934")
rectangleCalculateButton = ttk.Button(
    rectangleButtonsFrame, text="Calculate")
rectangleResetButton = ttk.Button(
    rectangleButtonsFrame, text="Reset", command=reset)

# Triangle
triangleEdge1Frame = Frame(root, bg="#272934")
triangleEdge1Label = ttk.Label(triangleEdge1Frame, text="Edge 1:", font=(
    "Calibri", 14), background="#272934", foreground="white")
triangleEdge1Inputbox = Entry(triangleEdge1Frame, width=8)
triangleEdge1MetricOptions = ["cm", "inch", "feet", "cm", "m"]
triangleEdge1MetricPlaceholder = StringVar()
triangleEdge1MetricPlaceholder.set(triangleEdge1MetricOptions[0])

triangleEdge1MetricDropdown = ttk.OptionMenu(
    triangleEdge1Frame, triangleEdge1MetricPlaceholder, *triangleEdge1MetricOptions)

triangleEdge2Frame = Frame(root, bg="#272934")
triangleEdge2Label = ttk.Label(triangleEdge2Frame, text="Edge 2:", font=(
    "Calibri", 14), background="#272934", foreground="white")
triangleEdge2Inputbox = Entry(triangleEdge2Frame, width=8)
triangleEdge2MetricOptions = ["cm", "inch", "feet", "cm", "m"]
triangleEdge2MetricPlaceholder = StringVar()
triangleEdge2MetricPlaceholder.set(triangleEdge2MetricOptions[0])

triangleEdge2MetricDropdown = ttk.OptionMenu(
    triangleEdge2Frame, triangleEdge2MetricPlaceholder, *triangleEdge2MetricOptions)

triangleEdge3Frame = Frame(root, bg="#272934")
triangleEdge3Label = ttk.Label(triangleEdge3Frame, text="Edge 3:", font=(
    "Calibri", 14), background="#272934", foreground="white")
triangleEdge3Inputbox = Entry(triangleEdge3Frame, width=8)
triangleEdge3MetricOptions = ["cm", "inch", "feet", "cm", "m"]
triangleEdge3MetricPlaceholder = StringVar()
triangleEdge3MetricPlaceholder.set(triangleEdge3MetricOptions[0])

triangleEdge3MetricDropdown = ttk.OptionMenu(
    triangleEdge3Frame, triangleEdge3MetricPlaceholder, *triangleEdge3MetricOptions)

triangleButtonsFrame = Frame(root, bg="#272934")
triangleCalculateButton = ttk.Button(triangleButtonsFrame, text="Calculate")
triangleResetButton = ttk.Button(
    triangleButtonsFrame, text="Reset", command=reset)

# Circle Semi-Cricle
radiusFrame = Frame(root, bg="#272934")
radiusLabel = ttk.Label(radiusFrame, text="Radius:", font=(
    "Calibri", 14), background="#272934", foreground="white")
radiusInputbox = Entry(radiusFrame, width=8)
radiusMetricOptions = ["cm", "inch", "feet", "cm", "m"]
radiusMetricPlaceholder = StringVar()
radiusMetricPlaceholder.set(radiusMetricOptions[0])

radiusMetricDropdown = ttk.OptionMenu(
    radiusFrame, radiusMetricPlaceholder, *radiusMetricOptions)

circleButtonsFrame = Frame(root, bg="#272934")
circleCalculateButton = ttk.Button(circleButtonsFrame, text="Calculate")
circleResetButton = ttk.Button(circleButtonsFrame, text="Reset", command=reset)

# Sector
sectorRadiusFrame = Frame(root, bg="#272934")
sectorRadiusLabel = ttk.Label(sectorRadiusFrame, text="Radius:", font=(
    "Calibri", 14), background="#272934", foreground="white")
sectorRadiusInputbox = Entry(sectorRadiusFrame, width=8)
sectorRadiusMetricOptions = ["cm", "inch", "feet", "cm", "m"]
sectorRadiusMetricPlaceholder = StringVar()
sectorRadiusMetricPlaceholder.set(sectorRadiusMetricOptions[0])

sectorRadiusMetricDropdown = ttk.OptionMenu(
    sectorRadiusFrame, sectorRadiusMetricPlaceholder, *sectorRadiusMetricOptions)

sectorAngleFrame = Frame(root, bg="#272934")
sectorAngleLabel = ttk.Label(sectorAngleFrame, text="Angle:", font=(
    "Calibri", 14), background="#272934", foreground="white")
sectorAngleInputbox = Entry(sectorAngleFrame, width=8)
sectorAngleMetricOptions = ["cm", "inch", "feet", "cm", "m"]
sectorAngleMetricPlaceholder = StringVar()
sectorAngleMetricPlaceholder.set(sectorAngleMetricOptions[0])

sectorAngleMetricDropdown = ttk.OptionMenu(
    sectorAngleFrame, sectorAngleMetricPlaceholder, *sectorAngleMetricOptions)

sectorButtonsFrame = Frame(root, bg="#272934")
sectorCalculateButton = ttk.Button(sectorButtonsFrame, text="Calculate")
sectorResetButton = ttk.Button(sectorButtonsFrame, text="Reset", command=reset)

# Ellipse
majorAxisFrame = Frame(root, bg="#272934")
majorAxisLabel = ttk.Label(majorAxisFrame, text="Semi-major Axes:", font=(
    "Calibri", 14), background="#272934", foreground="white")
majorAxisInputbox = Entry(majorAxisFrame, width=8)
majorAxisMetricOptions = ["cm", "inch", "feet", "cm", "m"]
majorAxisMetricPlaceholder = StringVar()
majorAxisMetricPlaceholder.set(majorAxisMetricOptions[0])

majorAxisMetricDropdown = ttk.OptionMenu(
    majorAxisFrame, majorAxisMetricPlaceholder, *majorAxisMetricOptions)

minorAxisFrame = Frame(root, bg="#272934")
minorAxisLabel = ttk.Label(minorAxisFrame, text="Semi-minor Axes:", font=(
    "Calibri", 14), background="#272934", foreground="white")
minorAxisInputbox = Entry(minorAxisFrame, width=8)
minorAxisMetricOptions = ["cm", "inch", "feet", "cm", "m"]
minorAxisMetricPlaceholder = StringVar()
minorAxisMetricPlaceholder.set(minorAxisMetricOptions[0])

minorAxisMetricDropdown = ttk.OptionMenu(
    minorAxisFrame, minorAxisMetricPlaceholder, *minorAxisMetricOptions)

ellipseButtonsFrame = Frame(root, bg="#272934")
ellpiseCalculateButton = ttk.Button(ellipseButtonsFrame, text="Calculate")
ellipseResetButton = ttk.Button(
    ellipseButtonsFrame, text="Reset", command=reset)

# Trapezoid
trapezoidBase1Frame = Frame(root, bg="#272934")
trapezoidBase1Label = ttk.Label(trapezoidBase1Frame, text="Base 1:", font=(
    "Calibri", 14), background="#272934", foreground="white")
trapezoidBase1Inputbox = Entry(trapezoidBase1Frame, width=8)
trapezoidBase1MetricOptions = ["cm", "inch", "feet", "cm", "m"]
trapezoidBase1MetricPlaceholder = StringVar()
trapezoidBase1MetricPlaceholder.set(trapezoidBase1MetricOptions[0])

trapezoidBase1MetricDropdown = ttk.OptionMenu(
    trapezoidBase1Frame, trapezoidBase1MetricPlaceholder, *trapezoidBase1MetricOptions)

trapezoidBase2Frame = Frame(root, bg="#272934")
trapezoidBase2Label = ttk.Label(trapezoidBase2Frame, text="Edge 2:", font=(
    "Calibri", 14), background="#272934", foreground="white")
trapezoidBase2Inputbox = Entry(trapezoidBase2Frame, width=8)
trapezoidBase2MetricOptions = ["cm", "inch", "feet", "cm", "m"]
trapezoidBase2MetricPlaceholder = StringVar()
trapezoidBase2MetricPlaceholder.set(trapezoidBase2MetricOptions[0])

trapezoidBase2MetricDropdown = ttk.OptionMenu(
    trapezoidBase2Frame, trapezoidBase2MetricPlaceholder, *trapezoidBase2MetricOptions)

trapezoidHeightFrame = Frame(root, bg="#272934")
trapezoidHeightLabel = ttk.Label(trapezoidHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
trapezoidHeightInputbox = Entry(trapezoidHeightFrame, width=8)
trapezoidHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
trapezoidHeightMetricPlaceholder = StringVar()
trapezoidHeightMetricPlaceholder.set(trapezoidHeightMetricOptions[0])

trapezoidHeightMetricDropdown = ttk.OptionMenu(
    trapezoidHeightFrame, trapezoidHeightMetricPlaceholder, *trapezoidHeightMetricOptions)

trapezoidButtonsFrame = Frame(root, bg="#272934")
trapezoidCalculateButton = ttk.Button(trapezoidButtonsFrame, text="Calculate")
trapezoidResetButton = ttk.Button(
    trapezoidButtonsFrame, text="Reset", command=reset)

# Cuboid, Pyramid
cuboidPyramidLengthFrame = Frame(root, bg="#272934")
cuboidPyramidLengthLabel = ttk.Label(cuboidPyramidLengthFrame, text="Length:", font=(
    "Calibri", 14), background="#272934", foreground="white")
cuboidPyramidLengthInputbox = Entry(cuboidPyramidLengthFrame, width=8)
cuboidPyramidLengthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
cuboidPyramidLengthMetricPlaceholder = StringVar()
cuboidPyramidLengthMetricPlaceholder.set(cuboidPyramidLengthMetricOptions[0])

cuboidPyramidLengthMetricDropdown = ttk.OptionMenu(
    cuboidPyramidLengthFrame, cuboidPyramidLengthMetricPlaceholder, *cuboidPyramidLengthMetricOptions)

cuboidPyramidWidthFrame = Frame(root, bg="#272934")
cuboidPyramidWidthLabel = ttk.Label(cuboidPyramidWidthFrame, text="Width:", font=(
    "Calibri", 14), background="#272934", foreground="white")
cuboidPyramidWidthInputbox = Entry(cuboidPyramidWidthFrame, width=8)
cuboidPyramidWidthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
cuboidPyramidWidthMetricPlaceholder = StringVar()
cuboidPyramidWidthMetricPlaceholder.set(cuboidPyramidWidthMetricOptions[0])

cuboidPyramidWidthMetricDropdown = ttk.OptionMenu(
    cuboidPyramidWidthFrame, cuboidPyramidWidthMetricPlaceholder, *cuboidPyramidWidthMetricOptions)

cuboidPyramidHeightFrame = Frame(root, bg="#272934")
cuboidPyramidHeightLabel = ttk.Label(cuboidPyramidHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
cuboidPyramidHeightInputbox = Entry(cuboidPyramidHeightFrame, width=8)
cuboidPyramidHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
cuboidPyramidHeightMetricPlaceholder = StringVar()
cuboidPyramidHeightMetricPlaceholder.set(cuboidPyramidHeightMetricOptions[0])

cuboidPyramidHeightMetricDropdown = ttk.OptionMenu(
    cuboidPyramidHeightFrame, cuboidPyramidHeightMetricPlaceholder, *cuboidPyramidHeightMetricOptions)

cuboidPyramidButtonsFrame = Frame(root, bg="#272934")
cuboidPyramidCalculateButton = ttk.Button(
    cuboidPyramidButtonsFrame, text="Calculate")
cuboidPyramidResetButton = ttk.Button(
    cuboidPyramidButtonsFrame, text="Reset", command=reset)

# Cone, Cylinder
coneCylinderRadiusFrame = Frame(root, bg="#272934")
coneCylinderRadiusLabel = ttk.Label(coneCylinderRadiusFrame, text="Radius:", font=(
    "Calibri", 14), background="#272934", foreground="white")
coneCylinderRadiusInputbox = Entry(coneCylinderRadiusFrame, width=8)
coneCylinderRadiusMetricOptions = ["cm", "inch", "feet", "cm", "m"]
coneCylinderRadiusMetricPlaceholder = StringVar()
coneCylinderRadiusMetricPlaceholder.set(coneCylinderRadiusMetricOptions[0])

coneCylinderRadiusMetricDropdown = ttk.OptionMenu(
    coneCylinderRadiusFrame, coneCylinderRadiusMetricPlaceholder, *coneCylinderRadiusMetricOptions)

coneCylinderHeightFrame = Frame(root, bg="#272934")
coneCylinderHeightLabel = ttk.Label(coneCylinderHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
coneCylinderHeightInputbox = Entry(coneCylinderHeightFrame, width=8)
coneCylinderHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
coneCylinderHeightMetricPlaceholder = StringVar()
coneCylinderHeightMetricPlaceholder.set(coneCylinderHeightMetricOptions[0])

coneCylinderHeightMetricDropdown = ttk.OptionMenu(
    coneCylinderHeightFrame, coneCylinderHeightMetricPlaceholder, *coneCylinderHeightMetricOptions)

coneCylinderButtonsFrame = Frame(root, bg="#272934")
coneCylinderCalculateButton = ttk.Button(
    coneCylinderButtonsFrame, text="Calculate")
coneCylinderResetButton = ttk.Button(
    coneCylinderButtonsFrame, text="Reset", command=reset)

resultFrame = Frame(root, bg="#272934")

root.mainloop()
