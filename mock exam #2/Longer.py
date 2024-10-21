"""Longer"""
import math
def main(radius, a, b):
    """main Longer"""
    circle = 2 * math.pi * radius
    rectangle = 2 * (a + b)
    if circle > rectangle:
        print("Circle is longer")
    elif rectangle > circle:
        print("Rectangle is longer")
    else:
        print("Equal")
    difference = abs(circle - rectangle)
    print(f"{difference:.5f}")
main(float(input()), float(input()), float(input()))
