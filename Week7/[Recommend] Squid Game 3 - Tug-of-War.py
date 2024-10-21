"""[Recommend] Squid Game 3 - Tug-of-War"""
def main():
    """Main [Recommend] Squid Game 3 - Tug-of-War"""
    team_a_total = 0
    team_b_total = 0
    for _ in range(10):
        force_a = int(input())
        team_a_total += force_a
    for _ in range(10):
        force_b = int(input())
        team_b_total += force_b
    if team_a_total > team_b_total:
        print("B")
    elif team_b_total > team_a_total:
        print("A")
    else:
        print("AB")
main()
