"""PickThem"""
def main():
    """main PickThem"""
    input_data = input().strip("[]")
    numbers = list(map(int, input_data.split(',')))
    even_numbers = [num for num in numbers if not num % 2]
    if even_numbers:
        for num in even_numbers:
            print(num)
    else:
        print("Nope")
main()
