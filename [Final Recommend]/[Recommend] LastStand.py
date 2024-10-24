"""LastStand"""
def main():
    """main LastStand"""
    numbers = input().strip('[]').split(',')
    for num in numbers:
        print(num.strip()[-1])
main()
