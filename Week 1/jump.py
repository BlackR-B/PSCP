"""yaa"""
def output(num, count=0):
    """Jump"""
    if count < 3:
        print(f"Output{num}")
        output(num, count + 1)

def jumping(num=1):
    """Jumping"""
    if num <= 4:
        output(num)
        jumping(num + 1)

jumping()
