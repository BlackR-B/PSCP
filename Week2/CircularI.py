"""Circular I"""
import math
def main():
    """find mosqito"""
    x = float(input())
    y = float(input())
    r = float(input())
    xm = float(input())
    ym = float(input())
    point = (math.sqrt(((xm - x) ** 2) + ((ym - y) ** 2)))
    if point > r:
        print("No")
    else:
        print("Yes")
main()
