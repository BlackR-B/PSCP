"""Hannae It's Even"""
def main():
    """Find Even"""
    numbers = []
    for _ in range(8):
        try:
            number = int(input())
            numbers.append(number)
        except ValueError:
            break
    for number in numbers:
        if not number % 2 :
            print(number)
main()
