"""[Mock Final 2023] Alcohol"""
def calculate_bac(sex, weight, has_license, drink_volume, alcohol_percentage, can_count, hours_rest):
    """[Mock Final 2023] Alcohol"""
    if sex == "Male":
        bac = (drink_volume * alcohol_percentage / 100 * can_count) / (weight * 0.68)
    else:
        bac = (drink_volume * alcohol_percentage / 100 * can_count) / (weight * 0.55)
    bac -= hours_rest * 0.015
    return bac, has_license
def main():
    """[Mock Final 2023] Alcohol"""
    sex = input().strip()
    weight = float(input().strip())
    has_license = input().strip() == "Yes"
    drink_volume = float(input().strip())
    alcohol_percentage = float(input().strip())
    can_count = int(input().strip())
    hours_rest = int(input().strip())
    bac, has_license = calculate_bac(sex, weight, has_license, drink_volume, alcohol_percentage, can_count, hours_rest)
    if has_license and bac <= 0.05:
        print("Safe")
    else:
        print("Not Safe")
main()
