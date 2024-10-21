"""Day I"""
def main():
    """calculate Day I"""
    year = int(input())
    if not year % 4 and year % 100:
        print("Yes")
    elif not year % 400:
        print("Yes")
    else:
        print("No")
main()
