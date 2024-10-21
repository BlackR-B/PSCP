"""PhoneNumber"""
def main(telephon_number, teltype):
    """main PhoneNumber"""
    if teltype == "Domestic":
        if len(telephon_number) == 9:
            telephone_number3 = telephon_number[5:]
            telephone_number2 = telephon_number[1:5]
            print(f"0 {telephone_number2} {telephone_number3}")
        elif len(telephon_number) == 10:
            telephone_number3 = telephon_number[6:]
            telephone_number2 = telephon_number[2:6]
            print(f"0{telephon_number[1]} {telephone_number2} {telephone_number3}")
    elif teltype == "International":
        if len(telephon_number) == 9:
            telephone_number3 = telephon_number[5:]
            telephone_number2 = telephon_number[1:5]
            print(f"+66 {telephone_number2} {telephone_number3}")
        elif len(telephon_number) == 10:
            telephone_number3 = telephon_number[6:]
            telephone_number2 = telephon_number[2:6]
            print(f"+66{telephon_number[1]} {telephone_number2} {telephone_number3}")
main(input(), input())
