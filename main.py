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
    resultFrame.pack_forget()
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


def sideReset():
    sideInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def sideButton():
    if(answer == "Square"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            squareArea = input * input
            resultLabel.config(
                text=f"Area = {squareArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    else:
        resultFrame.pack_forget()

    if(answer == "Pentagon"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            pentagonArea = (
                math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * input * input) / 4
            resultLabel.config(
                text=f"Area = {pentagonArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Hexagon"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            hexagonArea = ((3 * math.sqrt(3) * (input * input)) / 2)
            resultLabel.config(
                text=f"Area = {hexagonArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Octagon"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            octagonArea = (2 * (1 + (math.sqrt(2))) * input * input)
            resultLabel.config(
                text=f"Area = {octagonArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Cube"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            cubeArea = 6 * input ** 2
            cubeVolume = input ** 3
            resultLabel.config(
                text=f"Surface Area = {cubeArea}cm2\n Volume = {cubeVolume}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Tetrahedron"):
        if(sideInputbox.get().isdigit()):
            input = int(sideInputbox.get())
            tetrahedronArea = math.sqrt(3) * (input ** 2)
            tetrahedronVolume = (input ** 3) / 6 * math.sqrt(2)
            resultLabel.config(
                text=f"Surface Area = {tetrahedronArea}cm2\nVolume = {tetrahedronVolume}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def rectangleButton():
    if(answer == "Rectangle"):
        if(rectangleLengthInputbox.get().isdigit() and rectangleWidthInputbox.get().isdigit()):
            lengthInput = int(rectangleLengthInputbox.get())
            widthInput = int(rectangleWidthInputbox.get())
            rectangleArea = lengthInput * widthInput
            resultLabel.config(
                text=f" Area = {rectangleArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def rectangleReset():
    rectangleLengthInputbox.delete(0, END)
    rectangleWidthInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def triangleButton():
    if(answer == "Triangle"):
        if(triangleEdge1Inputbox.get().isdigit() and triangleEdge2Inputbox.get().isdigit() and triangleEdge3Inputbox.get().isdigit()):
            edge1 = int(triangleEdge1Inputbox.get())
            edge2 = int(triangleEdge2Inputbox.get())
            edge3 = int(triangleEdge3Inputbox.get())
            s = (edge1 + edge2 + edge3) / 2
            triangleArea = (s * (s - edge1) * (s - edge2) * (s - edge3)) ** 0.5
            resultLabel.config(
                text=f" Area = {triangleArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def triangleReset():
    triangleEdge1Inputbox.delete(0, END)
    triangleEdge2Inputbox.delete(0, END)
    triangleEdge3Inputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def radiusButton():
    if(answer == "Circle"):
        if(radiusInputbox.get().isdigit()):
            radiusInput = int(radiusInputbox.get())
            circleArea = 3.14 * (radiusInput * radiusInput)
            resultLabel.config(
                text=f" Area = {circleArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Semi-Circle"):
        if(radiusInputbox.get().isdigit()):
            radiusInput = int(radiusInputbox.get())
            semiCircleArea = 0.5 * 3.14 * (radiusInput * radiusInput)
            resultLabel.config(
                text=f" Area = {semiCircleArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Sphere"):
        if(radiusInputbox.get().isdigit()):
            radiusInput = int(radiusInputbox.get())
            sphereArea = 4 * 3.14 * (radiusInput ** 2)
            sphereVolume = 1.333 * 3.14 * (radiusInput ** 3)
            resultLabel.config(
                text=f" Area = {sphereArea}cm2\nVolume = {sphereVolume}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return
    if(answer == "Hemisphere"):
        if(radiusInputbox.get().isdigit()):
            radiusInput = int(radiusInputbox.get())
            hemiSphereArea = 2 * 3.14 * (radiusInput ** 2)
            hemiSphereVol = 0.6667 * 3.14 * (radiusInput ** 3)
            resultLabel.config(
                text=f" Area = {hemiSphereArea}cm2\nVolume = {hemiSphereVol}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def radiusReset():
    radiusInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def sectorButton():
    if(answer == "Sector"):
        if(sectorRadiusInputbox.get().isdigit() and sectorAngleInputbox.get().isdigit()):
            angleInput = int(sectorAngleInputbox.get())
            radiusInput = int(sectorRadiusInputbox.get())
            sectorArea = 3.14 * radiusInput * radiusInput * angleInput / 360
            resultLabel.config(
                text=f" Area = {sectorArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def sectorReset():
    sectorAngleInputbox.delete(0, END)
    sectorRadiusInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def ellipseButton():
    if(answer == "Ellipse"):
        if(majorAxisInputbox.get().isdigit() and minorAxisInputbox.get().isdigit()):
            majorInput = int(majorAxisInputbox.get())
            minorInput = int(minorAxisInputbox.get())
            ellipseArea = 3.14 * majorInput * minorInput
            resultLabel.config(
                text=f" Area = {ellipseArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def ellipseReset():
    majorAxisInputbox.delete(0, END)
    minorAxisInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def trapezoidButton():
    if(answer == "Trapezoid"):
        if(trapezoidBase1Inputbox.get().isdigit() and trapezoidBase2Inputbox.get().isdigit() and trapezoidHeightInputbox.get().isdigit()):
            base1 = int(trapezoidBase1Inputbox.get())
            base2 = int(trapezoidBase2Inputbox.get())
            height = int(trapezoidHeightInputbox.get())
            trapezoidArea = (base1 + base2) / 2 * height
            resultLabel.config(
                text=f" Area = {trapezoidArea}cm2")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def trapezoidReset():
    trapezoidBase1Inputbox.delete(0, END)
    trapezoidBase2Inputbox.delete(0, END)
    trapezoidHeightInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def cuboidPyramidButton():
    if(answer == "Cuboid"):
        if(cuboidPyramidLengthInputbox.get().isdigit() and cuboidPyramidWidthInputbox.get().isdigit() and cuboidPyramidHeightInputbox.get().isdigit()):
            length = int(cuboidPyramidLengthInputbox.get())
            width = int(cuboidPyramidWidthInputbox.get())
            height = int(cuboidPyramidHeightInputbox.get())
            cuboidArea = 2 * (length * width + width *
                              height + length * height)
            cuboidVolume = length * width * height
            resultLabel.config(
                text=f" Surface Area = {cuboidArea}cm2\nVolume = {cuboidVolume}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return

    if(answer == "Pyramid"):
        if(cuboidPyramidLengthInputbox.get().isdigit() and cuboidPyramidWidthInputbox.get().isdigit() and cuboidPyramidHeightInputbox.get().isdigit()):
            length = int(cuboidPyramidLengthInputbox.get())
            width = int(cuboidPyramidWidthInputbox.get())
            height = int(cuboidPyramidHeightInputbox.get())
            pyramidArea = length * width + length * \
                math.sqrt((width/2)**2 + height**2) + width * \
                math.sqrt((length/2)**2 + height ** 2)
            pyramidVolume = (length * width * height) / 3
            resultLabel.config(
                text=f" Surface Area = {pyramidArea}cm2\nVolume = {pyramidVolume}cm3")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def cuboidPyramidReset():
    cuboidPyramidLengthInputbox.delete(0, END)
    cuboidPyramidWidthInputbox.delete(0, END)
    cuboidPyramidHeightInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()


def coneCylinderButton():
    if(answer == "Cone"):
        if(coneCylinderRadiusInputbox.get().isdigit() and coneCylinderHeightInputbox.get().isdigit()):
            radius = float(coneCylinderRadiusInputbox.get())
            height = float(coneCylinderHeightInputbox.get())
            coneArea = (3.14 * radius *
                        (radius + math.sqrt(height * height) + (radius*radius)))
            coneVolume = 0.333 * 3.14 * (radius ** 2) * height
            resultLabel.config(
                text=f" Surface Area = {coneArea}\nVolume = {coneVolume}")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return

    if(answer == "Cylinder"):
        if(coneCylinderRadiusInputbox.get().isdigit() and coneCylinderHeightInputbox.get().isdigit()):
            radius = int(coneCylinderRadiusInputbox.get())
            height = int(coneCylinderHeightInputbox.get())
            cylinderArea = 2 * 3.14 * radius * \
                height + 2 * 3.14 * (radius ** 2)
            cylinderVolume = 3.14 * (radius ** 2) * height
            resultLabel.config(
                text=f" Surface Area = {cylinderArea}\nVolume = {cylinderVolume}")
            resultFrame.pack(side="top", fill="both")
            resultLabel.pack(side="top", pady=(50, 0))
        else:
            return


def coneCylinderReset():
    coneCylinderRadiusInputbox.delete(0, END)
    coneCylinderHeightInputbox.delete(0, END)
    resultLabel.config(text=" ")
    resultFrame.pack_forget()

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
sideMetricDropdown.config(state=DISABLED)

sideButtonsFrame = Frame(root, bg="#272934")
sideCalculateButton = ttk.Button(
    sideButtonsFrame, text="Calculate", command=sideButton)
sideResetButton = ttk.Button(sideButtonsFrame, text="Reset", command=sideReset)

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
rectangleLengthMetricDropdown.config(state=DISABLED)

rectangleWidthFrame = Frame(root, bg="#272934")
rectangleWidthLabel = ttk.Label(rectangleWidthFrame, text="Width:", font=(
    "Calibri", 14), background="#272934", foreground="white")
rectangleWidthInputbox = Entry(rectangleWidthFrame, width=8)
rectangleWidthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
rectangleWidthMetricPlaceholder = StringVar()
rectangleWidthMetricPlaceholder.set(rectangleWidthMetricOptions[0])

rectangleWidthMetricDropdown = ttk.OptionMenu(
    rectangleWidthFrame, rectangleWidthMetricPlaceholder, *rectangleWidthMetricOptions)
rectangleWidthMetricDropdown.config(state=DISABLED)

rectangleButtonsFrame = Frame(root, bg="#272934")
rectangleCalculateButton = ttk.Button(
    rectangleButtonsFrame, text="Calculate", command=rectangleButton)
rectangleResetButton = ttk.Button(
    rectangleButtonsFrame, text="Reset", command=rectangleReset)

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
triangleEdge1MetricDropdown.config(state=DISABLED)

triangleEdge2Frame = Frame(root, bg="#272934")
triangleEdge2Label = ttk.Label(triangleEdge2Frame, text="Edge 2:", font=(
    "Calibri", 14), background="#272934", foreground="white")
triangleEdge2Inputbox = Entry(triangleEdge2Frame, width=8)
triangleEdge2MetricOptions = ["cm", "inch", "feet", "cm", "m"]
triangleEdge2MetricPlaceholder = StringVar()
triangleEdge2MetricPlaceholder.set(triangleEdge2MetricOptions[0])

triangleEdge2MetricDropdown = ttk.OptionMenu(
    triangleEdge2Frame, triangleEdge2MetricPlaceholder, *triangleEdge2MetricOptions)
triangleEdge2MetricDropdown.config(state=DISABLED)

triangleEdge3Frame = Frame(root, bg="#272934")
triangleEdge3Label = ttk.Label(triangleEdge3Frame, text="Edge 3:", font=(
    "Calibri", 14), background="#272934", foreground="white")
triangleEdge3Inputbox = Entry(triangleEdge3Frame, width=8)
triangleEdge3MetricOptions = ["cm", "inch", "feet", "cm", "m"]
triangleEdge3MetricPlaceholder = StringVar()
triangleEdge3MetricPlaceholder.set(triangleEdge3MetricOptions[0])

triangleEdge3MetricDropdown = ttk.OptionMenu(
    triangleEdge3Frame, triangleEdge3MetricPlaceholder, *triangleEdge3MetricOptions)
triangleEdge3MetricDropdown.config(state=DISABLED)

triangleButtonsFrame = Frame(root, bg="#272934")
triangleCalculateButton = ttk.Button(
    triangleButtonsFrame, text="Calculate", command=triangleButton)
triangleResetButton = ttk.Button(
    triangleButtonsFrame, text="Reset", command=triangleReset)

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
radiusMetricDropdown.config(state=DISABLED)

circleButtonsFrame = Frame(root, bg="#272934")
circleCalculateButton = ttk.Button(
    circleButtonsFrame, text="Calculate", command=radiusButton)
circleResetButton = ttk.Button(
    circleButtonsFrame, text="Reset", command=radiusReset)

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
sectorRadiusMetricDropdown.config(state=DISABLED)

sectorAngleFrame = Frame(root, bg="#272934")
sectorAngleLabel = ttk.Label(sectorAngleFrame, text="Angle:", font=(
    "Calibri", 14), background="#272934", foreground="white")
sectorAngleInputbox = Entry(sectorAngleFrame, width=8)
sectorAngleMetricOptions = ["cm", "inch", "feet", "cm", "m"]
sectorAngleMetricPlaceholder = StringVar()
sectorAngleMetricPlaceholder.set(sectorAngleMetricOptions[0])

sectorAngleMetricDropdown = ttk.OptionMenu(
    sectorAngleFrame, sectorAngleMetricPlaceholder, *sectorAngleMetricOptions)
sectorAngleMetricDropdown.config(state=DISABLED)

sectorButtonsFrame = Frame(root, bg="#272934")
sectorCalculateButton = ttk.Button(
    sectorButtonsFrame, text="Calculate", command=sectorButton)
sectorResetButton = ttk.Button(
    sectorButtonsFrame, text="Reset", command=sectorReset)

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
majorAxisMetricDropdown.config(state=DISABLED)

minorAxisFrame = Frame(root, bg="#272934")
minorAxisLabel = ttk.Label(minorAxisFrame, text="Semi-minor Axes:", font=(
    "Calibri", 14), background="#272934", foreground="white")
minorAxisInputbox = Entry(minorAxisFrame, width=8)
minorAxisMetricOptions = ["cm", "inch", "feet", "cm", "m"]
minorAxisMetricPlaceholder = StringVar()
minorAxisMetricPlaceholder.set(minorAxisMetricOptions[0])

minorAxisMetricDropdown = ttk.OptionMenu(
    minorAxisFrame, minorAxisMetricPlaceholder, *minorAxisMetricOptions)
minorAxisMetricDropdown.config(state=DISABLED)

ellipseButtonsFrame = Frame(root, bg="#272934")
ellpiseCalculateButton = ttk.Button(
    ellipseButtonsFrame, text="Calculate", command=ellipseButton)
ellipseResetButton = ttk.Button(
    ellipseButtonsFrame, text="Reset", command=ellipseReset)

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
trapezoidBase1MetricDropdown.config(state=DISABLED)

trapezoidBase2Frame = Frame(root, bg="#272934")
trapezoidBase2Label = ttk.Label(trapezoidBase2Frame, text="Edge 2:", font=(
    "Calibri", 14), background="#272934", foreground="white")
trapezoidBase2Inputbox = Entry(trapezoidBase2Frame, width=8)
trapezoidBase2MetricOptions = ["cm", "inch", "feet", "cm", "m"]
trapezoidBase2MetricPlaceholder = StringVar()
trapezoidBase2MetricPlaceholder.set(trapezoidBase2MetricOptions[0])

trapezoidBase2MetricDropdown = ttk.OptionMenu(
    trapezoidBase2Frame, trapezoidBase2MetricPlaceholder, *trapezoidBase2MetricOptions)
trapezoidBase2MetricDropdown.config(state=DISABLED)

trapezoidHeightFrame = Frame(root, bg="#272934")
trapezoidHeightLabel = ttk.Label(trapezoidHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
trapezoidHeightInputbox = Entry(trapezoidHeightFrame, width=8)
trapezoidHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
trapezoidHeightMetricPlaceholder = StringVar()
trapezoidHeightMetricPlaceholder.set(trapezoidHeightMetricOptions[0])

trapezoidHeightMetricDropdown = ttk.OptionMenu(
    trapezoidHeightFrame, trapezoidHeightMetricPlaceholder, *trapezoidHeightMetricOptions)
trapezoidHeightMetricDropdown.config(state=DISABLED)

trapezoidButtonsFrame = Frame(root, bg="#272934")
trapezoidCalculateButton = ttk.Button(
    trapezoidButtonsFrame, text="Calculate", command=trapezoidButton)
trapezoidResetButton = ttk.Button(
    trapezoidButtonsFrame, text="Reset", command=trapezoidReset)

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
cuboidPyramidLengthMetricDropdown.config(state=DISABLED)

cuboidPyramidWidthFrame = Frame(root, bg="#272934")
cuboidPyramidWidthLabel = ttk.Label(cuboidPyramidWidthFrame, text="Width:", font=(
    "Calibri", 14), background="#272934", foreground="white")
cuboidPyramidWidthInputbox = Entry(cuboidPyramidWidthFrame, width=8)
cuboidPyramidWidthMetricOptions = ["cm", "inch", "feet", "cm", "m"]
cuboidPyramidWidthMetricPlaceholder = StringVar()
cuboidPyramidWidthMetricPlaceholder.set(cuboidPyramidWidthMetricOptions[0])

cuboidPyramidWidthMetricDropdown = ttk.OptionMenu(
    cuboidPyramidWidthFrame, cuboidPyramidWidthMetricPlaceholder, *cuboidPyramidWidthMetricOptions)
cuboidPyramidWidthMetricDropdown.config(state=DISABLED)

cuboidPyramidHeightFrame = Frame(root, bg="#272934")
cuboidPyramidHeightLabel = ttk.Label(cuboidPyramidHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
cuboidPyramidHeightInputbox = Entry(cuboidPyramidHeightFrame, width=8)
cuboidPyramidHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
cuboidPyramidHeightMetricPlaceholder = StringVar()
cuboidPyramidHeightMetricPlaceholder.set(cuboidPyramidHeightMetricOptions[0])

cuboidPyramidHeightMetricDropdown = ttk.OptionMenu(
    cuboidPyramidHeightFrame, cuboidPyramidHeightMetricPlaceholder, *cuboidPyramidHeightMetricOptions)
cuboidPyramidHeightMetricDropdown.config(state=DISABLED)

cuboidPyramidButtonsFrame = Frame(root, bg="#272934")
cuboidPyramidCalculateButton = ttk.Button(
    cuboidPyramidButtonsFrame, text="Calculate", command=cuboidPyramidButton)
cuboidPyramidResetButton = ttk.Button(
    cuboidPyramidButtonsFrame, text="Reset", command=cuboidPyramidReset)

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
coneCylinderRadiusMetricDropdown.config(state=DISABLED)

coneCylinderHeightFrame = Frame(root, bg="#272934")
coneCylinderHeightLabel = ttk.Label(coneCylinderHeightFrame, text="Height:", font=(
    "Calibri", 14), background="#272934", foreground="white")
coneCylinderHeightInputbox = Entry(coneCylinderHeightFrame, width=8)
coneCylinderHeightMetricOptions = ["cm", "inch", "feet", "cm", "m"]
coneCylinderHeightMetricPlaceholder = StringVar()
coneCylinderHeightMetricPlaceholder.set(coneCylinderHeightMetricOptions[0])

coneCylinderHeightMetricDropdown = ttk.OptionMenu(
    coneCylinderHeightFrame, coneCylinderHeightMetricPlaceholder, *coneCylinderHeightMetricOptions)
coneCylinderHeightMetricDropdown.config(state=DISABLED)

coneCylinderButtonsFrame = Frame(root, bg="#272934")
coneCylinderCalculateButton = ttk.Button(
    coneCylinderButtonsFrame, text="Calculate", command=coneCylinderButton)
coneCylinderResetButton = ttk.Button(
    coneCylinderButtonsFrame, text="Reset", command=coneCylinderReset)

resultFrame = Frame(root, bg="#272934")
resultLabel = ttk.Label(resultFrame, text="Area =", font=(
    "Calibri", 14), background="#272934", foreground="white")

root.mainloop()
