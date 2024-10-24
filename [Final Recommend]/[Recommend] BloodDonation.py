"""BloodDonation"""
def main():
    """Main BloodDonation"""
    age = int(input())
    weight = int(input())
    donation = int(input())
    case1 = False
    case4 = False
    if age == 17 or 60 <= age <= 70:
        paper = input()
        case1 = age == 17 and weight>=45 and paper == "True"
        case4 = 60 <= age <= 70 and weight >= 45 and donation and paper == "True"
    case2 = 17 < age <= 55 and weight >= 45
    case3 = 55 < age < 60 and weight >= 45 and donation
    if case1 or case2 or case3 or case4:
        print("Yes")
    else:
        print("No")
main()
