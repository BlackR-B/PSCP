"""[Final 2019] WPM"""
def kids(wpm):
    """Main kids"""
    if wpm < 11:
        return "Very Slow"
    if 11 <= wpm <= 20:
        return "Slow"
    if 21 <= wpm <= 30:
        return "Average"
    if 31 <= wpm <= 40:
        return "Fast"
    return "Very Fast"
def adults(wpm):
    """Main adults"""
    if wpm < 26:
        return "Very Slow"
    if 26 <= wpm <= 35:
        return "Slow/Beginner"
    if 36 <= wpm <= 45:
        return "Intermediate/Average"
    if 46 <= wpm <= 65:
        return "Fast/Advanced"
    if 66 <= wpm <= 80:
        return "Very Fast"
    return "Insane"
def main():
    """Main [Final 2019] WPM"""
    group = input()
    wpm = int(input())
    category = None
    if group == "Kids":
        category = kids(wpm)
    elif group == "Adults":
        category = adults(wpm)
    print(category)
main()
