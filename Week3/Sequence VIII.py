"""Sequence VIII"""
def main(num):
    """main"""
    for i in range(num):
        print(" " * (3 * (num - i - 1)), end="")
        for j in range(i+1):
            if i >= j:
                print(f"{j+1:>02}", end=" ")
            else:
                print("", end="")
        print()
main(int(input()))
