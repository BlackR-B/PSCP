"""Mock Midterm 2023  Recommend Lift"""
def lift():
    """main Mock Midterm 2023  Recommend Lift"""
    human = int(input())
    value = float(input())
    total_weight = 0
    has_adult = 0
    has_child = 0
    for _ in range(human):
        age = int(input())
        weight = float(input())
        total_weight += weight
        if age < 12:
            has_child += 1
        else:
            has_adult += 1
    if (has_child and not has_adult) or total_weight > value:
        print("Not Safe")
    else:
        print("Safe")
lift()
