"""[Final 2019] Tax"""
def main():
    """Main [Final 2019] Tax"""
    age = int(input())
    cc = int(input())
    if cc <= 600:
        tax = cc * 0.50
    elif 600 < cc <= 1800:
        tax = 600 * 0.50 + (cc - 600) * 1.50
    else:
        tax = 600 * 0.50 + 1200 * 1.50 + (cc - 1800) * 4.00
    if age >= 10:
        discount = 0.50
    elif age == 9:
        discount = 0.40
    elif age == 8:
        discount = 0.30
    elif age == 7:
        discount = 0.20
    elif age == 6:
        discount = 0.10
    else:
        discount = 0.00
    total_tax = tax * (1 - discount)
    print(f"{total_tax:.2f}")
main()
