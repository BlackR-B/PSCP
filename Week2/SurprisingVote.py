"""SurprisingVote"""
def point(total, highest):
    """point of three"""
    second = min(total - highest , highest)
    lowest = total - highest - second
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
point(float(input()), float(input()))
