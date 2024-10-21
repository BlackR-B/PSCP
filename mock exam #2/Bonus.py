"""Bonus"""
def main(salary, years, months):
    """main Bonus"""
    if months >= 10:
        years += 1
    bonus = min(years, 20) * salary
    bonus = min(bonus, 1000000)
    bonus = max(bonus, 5000)
    print(bonus)
main(int(input()), int(input()), int(input()))
