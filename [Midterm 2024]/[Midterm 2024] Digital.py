"""[Midterm 2024] Digital"""
def main(name, thai, house, age, income, bank):
    """main [Midterm 2024] Digital"""
    if thai in ["Yes", "True"] and house in ["Yes", "True"] \
    and age >= 16 and income <= 840000 and bank <= 500000:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main(input(), input(), input(), float(input()), float(input()), float(input()),)
