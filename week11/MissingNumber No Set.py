"""MissingNumber No Set"""
def main():
    """Main MissingNumber No Set"""
    n = int(input())
    numbers = []
    num = int(input())
    while num:
        numbers.append(num)
        num = int(input())
    missing_numbers = []
    for i in range(1, n + 1):
        if i not in numbers:
            missing_numbers.append(i)
    for missing in missing_numbers:
        print(missing)
main()
