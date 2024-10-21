"""Ball"""
def calculate(high,bounce,limited):
    """Calculated"""
    bounces_count = 0
    while high > limited:
        high *= bounce
        bounces_count += 1
    return bounces_count
def main():
    """main"""
    highted = float(input())
    bounce = 3 / 5
    limited = 0.01
    totala = calculate(highted,bounce,limited)
    totala -= 1
    if totala == -1:
        print("0")
    else:
        print(totala)
main()
