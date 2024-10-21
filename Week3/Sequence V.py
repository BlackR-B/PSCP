"""Sequence V"""
def main(num):
    """main"""
    count_per_lines = 7
    count = 0
    for i in range(num, 0, -1):
        print(i, end = " ")
        count += 1
        if count == count_per_lines:
            print()
            count = 0
main(int(input()))
