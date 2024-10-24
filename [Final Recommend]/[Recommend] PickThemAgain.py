"""PickThemAgain"""
def main():
    """main PickThemAgain"""
    number = input().split()
    result = [int(num) for num in number if not num % 3 or not num % 5]
    if result:
        for num in reversed(result):
            print(num)
    else:
        print("Nope")
main()
