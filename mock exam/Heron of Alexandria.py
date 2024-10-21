"""Heron of Alexandria"""
def triangle(a, b, c):
    """triangel main"""
    side = (a + b + c) / 2
    area = (side * (side - a) * (side - b) * (side - c)) ** 0.5
    print(f"{area:.3f}")
triangle(float(input()), float(input()), float(input()))
