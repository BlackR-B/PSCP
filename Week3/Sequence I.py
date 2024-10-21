"""Sequence I"""
def main(row_and_col):
    """main"""
    for _ in range(row_and_col):
        for j in range(1, row_and_col + 1):
            print(j, end=" ")
        print()
main(int(input()))
