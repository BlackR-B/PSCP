"""MissingNumber"""
def main():
    """Main MissingNumber"""
    n = int(input())
    numbers = set()
    num = int(input())
    while num:
        numbers.add(num)
        num = int(input())
    missing_numbers = []
    for i in range(1, n + 1):
        if i not in numbers:
            missing_numbers.append(i)
    for missing in sorted(missing_numbers):
        print(missing)
main()
