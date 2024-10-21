"""Sequence N"""
def main(m):
    """main Sequence N"""
    for i in range(m):
        for j in range(m):
            if not j or j == m - 1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
