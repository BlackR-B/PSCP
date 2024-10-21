"""Circular II"""
import math
def main():
    """Find krung dud feun"""
    x = float(input())
    y = float(input())
    z = float(input())
    x1 = float(input())
    y2 = float(input())
    z3 = float(input())
    z4 = z + z3
    r = (math.sqrt(((x - x1)** 2) + ((y - y2)** 2)))
    if r < z4:
        print("Yes")
    else:
        print("No")
main()
