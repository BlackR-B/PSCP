"""[Midterm 2024] Coffee Shop"""
def main(coast, discount1, discount2, minimum, cup):
    """main [Midterm 2024] Coffee Shop"""
    promotion1 = (coast * (cup - 1)) * (discount1 / 100)
    if coast * cup >= minimum:
        promotion2 = (coast * cup) * (discount2/ 100)
        if promotion1 <= promotion2:
            print("2")
            print(f"{abs(promotion2 - (coast * cup)):.2f}")
        elif promotion2 < promotion1:
            print("1")
            print(f"{abs(promotion1 - (coast * cup)):.2f}")
main(float(input()), float(input()), float(input()), float(input()), int(input()))
