"""Right Arrow"""
def main(width, rows):
    """main"""
    mid = rows // 2
    for i in range(rows):
        if i <= mid:
            print(" " * i + "*" * width)
        else:
            print(" " * (rows - i - 1) + "*" * width)
main(int(input()), int(input()))
