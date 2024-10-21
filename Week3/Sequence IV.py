"""Sequence III"""
def main(num):
    """main"""
    count_number = 1
    for _ in range(num):
        for _ in range(num):
            print(count_number , end = " ")
            count_number += 1
        print()
main(int(input()))
