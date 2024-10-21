"""SequenceX"""
def main():
    """main"""
    ix = int(input())
    for i in range(1, ix+1):
        num = 1
        for _ in range(ix - i):
            print("   ", end="")
        for _ in range(1, i + 1):
            print(f"{num:02} ", end="")
            num += 1
        num -= 2
        for _ in range(1, i):
            print(f"{num:02} ", end="")
            num -= 1
        print()
    for i in range(ix-1, 0, -1):
        num = 1
        for _ in range(ix - i):
            print("   ", end="")
        for _ in range(1, i + 1):
            print(f"{num:02} ", end="")
            num += 1
        num -= 2
        for _ in range(1, i):
            print(f"{num:02} ", end="")
            num -= 1
        print()
main()
