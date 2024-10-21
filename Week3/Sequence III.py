"""Sequence III"""
def main(num):
    """main"""
    for i in range(num):
        for j in range(num):
            print(i + j + 2, end = " ")
        print()
main(int(input()))
