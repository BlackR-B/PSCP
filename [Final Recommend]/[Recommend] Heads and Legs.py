"""[Recommend] Heads and Legs"""
def find_rabbits_and_birds(animal_count, leg_count):
    """[Recommend] Heads and Legs"""
    rabbits = (leg_count - 2 * animal_count) / 2
    birds = animal_count - rabbits
    if rabbits < 0 or birds < 0 or rabbits != int(rabbits) or birds != int(birds):
        return "Impossible"
    return int(rabbits), int(birds)
def main():
    """[Recommend] Heads and Legs"""
    animal_count = int(input())
    leg_count = int(input())
    result = find_rabbits_and_birds(animal_count, leg_count)
    if result == "Impossible":
        print(result)
    else:
        print(result[0], result[1])
main()
