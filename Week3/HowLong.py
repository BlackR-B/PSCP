"""HowLong"""
def main():
    """main"""
    num = int(input())
    if not num:
        print(1)
        return
    num_str = str(abs(num))
    LoL = 0
    for _ in num_str:
        LoL += 1
    print(LoL)
main()
