'''Inflation'''
def main(price, year):
    ''' main Inflation'''
    for _ in range(year):
        price += price * 381 // 10000
    print(f"{price // 100}.{price % 100:>02}")
main(int(float(input())*100), int(input()))
