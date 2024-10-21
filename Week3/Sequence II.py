"""Sequence II"""
def main(num):
    """main"""
    for i in range(1, num + 1):
        double_odd = i ** 2
        print(double_odd, end = " ")
    print()
main(int(input()))
