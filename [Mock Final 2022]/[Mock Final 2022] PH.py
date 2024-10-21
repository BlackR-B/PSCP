"""[Mock Final 2022] PH"""
def main():
    """[Mock Final 2022] PH"""
    ph_value = float(input().strip())

    if ph_value < 0 or ph_value > 14:
        print("error")
    elif ph_value < 7:
        print("acidic")
    elif ph_value == 7:
        print("neutral")
    else:  # ph_value > 7
        print("akaline")
main()
