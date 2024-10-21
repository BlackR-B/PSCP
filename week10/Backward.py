"""Backward"""
def main():
    """Mian Backward"""
    data = []
    line = input()
    while line != "NULL":
        data.insert(0, line)
        line = input()
    for item in data:
        print(item)
main()
