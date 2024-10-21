"""Left Arrow"""
def arrow(width, rows):
    """arrow"""
    mid = rows // 2
    for i in range(rows):
        spaces = abs(mid - i)
        print(" " * spaces + "*" * width)
arrow(int(input()), int(input()))
