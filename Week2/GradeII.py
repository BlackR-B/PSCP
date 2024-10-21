"""point"""
def main():
    """Calculate grade based on point"""
    point = float(input())
    if point > 100 or point < 0:
        print("ERR")
    elif 95 <= point <= 100:
        print("A")
    elif 90 <= point < 95:
        print("B+")
    elif 85 <= point < 90:
        print("B")
    elif 80 <= point < 85:
        print("C+")
    elif 75 <= point < 80:
        print("C")
    elif 70 <= point < 75:
        print("D+")
    elif 65 <= point < 70:
        print("D")
    elif 60 <= point < 65:
        print("F+")
    elif 0 <= point < 60:
        print("F")
main()
