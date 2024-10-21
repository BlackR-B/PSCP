"""Real function for kid"""
def rectangle_area(h, w):
    """Calculate the area of a rectangle."""
    return h * w

def rectangle_perimeter(h, w):
    """Calculate the perimeter of a rectangle."""
    return 2 * (h + w)

def main():
    """Main function to read input and print area and perimeter."""
    h = int(input())
    w = int(input())
    area = rectangle_area(h, w)
    perimeter = rectangle_perimeter(h, w)
    print(area)
    print(perimeter)

main()
