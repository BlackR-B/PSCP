"""SumOfNumber"""
def target(target_sum):
    """main"""
    total_sum = 0
    stop_value = 0
    while not stop_value:
        number = int(input())
        if number == -1:
            stop_value = total_sum
        else:
            total_sum += number
            if total_sum == target_sum:
                stop_value = total_sum
    print(total_sum)
target(int(input()))
