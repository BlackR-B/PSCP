"""LineSorting"""
def main (n):
    """main LineSorting"""
    lines = []
    for _ in range(n):
        line = input()
        lines.append(line)
    lines.sort(key = len)
    for line in lines:
        print(line)
main(int(input()))
