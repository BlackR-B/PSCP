"""ChristmasTree"""
def main(n, m):
    """main ChristmasTree"""
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for _ in range(m):
        print(" " * (n - 2) + "---")
main(int(input()), int(input()))
