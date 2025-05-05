# inspiration code for Python Unit Testing Project
import math

def surfaceArea(rad):
    return 4 * math.pi * rad * rad

def volume(rad, unused = None): # to match signature used in GeometryCalcWeb
    return (4/3) * math.pi * rad**3

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\nThe Volume of the Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
