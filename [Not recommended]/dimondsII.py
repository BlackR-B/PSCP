"""di"""
def main():
    """monds"""
    m = int(input())
    n = int(input())
    rows = []
    for _ in range(m):
        row = list(map(int, input().strip().split()))
        rows.append(row)
    for i in range(m):
        maxrow = max(rows[i])
    print(maxrow)
        
main()
