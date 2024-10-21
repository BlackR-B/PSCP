"""Difference"""
def main():
    """Main Difference"""
    n = int(input())
    m = int(input())
    a = set()
    for _ in range(n):
        a.add(int(input()))
    b = set()
    for _ in range(m):
        b.add(int(input()))
    result = a - b
    print(*sorted(result))
main()
