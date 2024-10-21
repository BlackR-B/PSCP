"""calculation"""
def calculation(number):
    """main calculation"""
    if number == 1:
        return "1"
    result = '+'.join(str(i) for i in range(1, number + 1)) + '+'
    return result
LAST_TIME = calculation(int(input()))
print(len(LAST_TIME))
