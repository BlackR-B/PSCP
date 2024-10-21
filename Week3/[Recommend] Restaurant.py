"""[Recommend] Restaurant"""
def resturant_food(first_coast_food, promotion, discount, second_coast_food):
    """main resturant food"""
    total_price = first_coast_food + second_coast_food # ราคารวม
    result_2 = total_price - (total_price * discount/100) # โปร 2
    result_1 = first_coast_food - (first_coast_food * discount/100) # โปร 1
    if first_coast_food == promotion: # ถ้าราคาที่กินไป == promotion
        if first_coast_food == promotion and not second_coast_food: # ถ้าราคาที่กินไป == promotion และ ราคาที่ต้องกินเพิ่ม == 0
            print("Yes")
        elif result_1 == result_2: # ถ้าโปรโมชั่นเท่ากัน
            print("Yes")
        elif result_1 > result_2: # ถ้าโปรโมชั่นแรกมากกว่าโปร 2
            print(f"Yes {abs(result_1 - result_2):.3f}")
        elif result_1 < result_2: # ถ้าโปร 2 < โปรแรก
            print(f"No {abs(result_1 - result_2):.3f}")
    elif first_coast_food + second_coast_food >= promotion: # ถ้าโดนกินแล้วมากกว่าหรือเท่ากับ promotion 
        if first_coast_food == result_2: # ถ้าที่กิน == โปร 2
            print("Yes")
        elif first_coast_food > result_2: # ถ้าที่กิน > โปร 2
            print(f"Yes {abs(first_coast_food - result_2):.3f}")
        else: # ถ้าที่กิน < โปร2
            print(f"No {abs(first_coast_food - result_2):.3f}")
    else: # ถ้ากินแล้วน้อยกว่าหรือเท่ากับ promotion 
        print("Yes")
resturant_food(float(input()), float(input()), float(input()), float(input()))
