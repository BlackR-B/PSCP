"""Home Run"""
def main(n, player_distance):
    """main Home Run"""
    home_run = 0
    for _ in range(n):
        field_distance = float(input())
        if player_distance > field_distance:
            home_run += 1
    print(home_run)
main(int(input()), float(input()))
