"""Median"""
def main(n):
    """main Median"""
    numbers = [float(input()) for _ in range(n)]
    numbers.sort()
    if n % 2 == 1:
        median = numbers[n //2]
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        median = (middle1 + middle2) / 2
    print(f"{median:.3f}")
main(int(input()))
