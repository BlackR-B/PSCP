"""[Recommend] BTSMRT"""
def main(day_type, age, height):
    """Main [Recommend] BTSMRT"""
    if day_type == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        elif age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
    elif day_type == "Senior Day":
        if age < 14 and height < 90:
            print("FREE")
        elif age >= 60:
            print("FREE")
        else:
            print("PAY")
    elif day_type == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
main(input(), float(input()), float(input()))
