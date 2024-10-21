"""[Recommend] Restaurant"""
def resturant_food(first_coast_food, promotion, discount, second_coast_food):
    """main resturant food"""
    total_price = first_coast_food + second_coast_food
    result_2 = total_price - (total_price * discount/100)
    result_1 = first_coast_food - (first_coast_food * discount/100)
    if first_coast_food == promotion:
        if first_coast_food == promotion and not second_coast_food:
            print("Yes")
        elif result_1 == result_2:
            print("Yes")
        elif result_1 > result_2:
            print(f"Yes {abs(result_1 - result_2):.3f}")
        elif result_1 < result_2:
            print(f"No {abs(result_1 - result_2):.3f}")
    elif first_coast_food + second_coast_food >= promotion:
        if first_coast_food == result_2:
            print("Yes")
        elif first_coast_food > result_2:
            print(f"Yes {abs(first_coast_food - result_2):.3f}")
        else:
            print(f"No {abs(first_coast_food - result_2):.3f}")
    else:
        print("Yes")
resturant_food(float(input()), float(input()), float(input()), float(input()))
