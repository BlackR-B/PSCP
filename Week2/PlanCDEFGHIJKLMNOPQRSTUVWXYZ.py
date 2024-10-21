"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """choose"""
    ad = input()
    x = float(input())
    y = float(input())
    z = float(input())
    if ad == "Ascend":
        if x > y:
            x, y = y, x
        if y > z:
            y, z = z, y
        if x > y:
            x, y = y, x
    elif ad == "Descend":
        if x < y:
            x, y = y, x
        if y < z:
            y, z = z, y
        if x < y:
            x, y = y, x
    print(f"{x:.2f}, {y:.2f}, {z:.2f}")
main()
