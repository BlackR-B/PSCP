"""PickThemAgain"""
def main():
    """main PickThemAgain"""
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    result = [num for num in numbers if not num % 3 or not num % 5]
    if result:
        for num in reversed(result):
            print(num)
    else:
        print("Nope")
main()
