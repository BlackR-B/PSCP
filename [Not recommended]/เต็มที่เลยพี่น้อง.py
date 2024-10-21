"""Diamond II"""
def main(m, n):
    """main Diamond II"""
    diamond_valuse = []
    for _ in range(m):
        line = list(map(int, input().strip().split()))
        diamond_valuse.append(line)
    print(diamond_valuse)
    
main(int(input().strip()), int(input().strip()))
