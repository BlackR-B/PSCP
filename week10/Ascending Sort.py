"""Ascending Sort"""
def main(n):
    """mian Ascending Sort"""
    numbers = [int(input()) for _ in range(n)]
    numbers.sort()
    for number in numbers:
        print(number)
main(int(input()))
