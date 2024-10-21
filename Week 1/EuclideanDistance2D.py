"""da head"""
import math
def calculate(q1,q2,p1,p2):
    """FUnction"""
    matata = math.sqrt((q1 - p1)**2 + (q2 - p2)**2)
    return matata
def main():
    """main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    d = calculate(q1,q2,p1,p2)
    print(d)
main()
