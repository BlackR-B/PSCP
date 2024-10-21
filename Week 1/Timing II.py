"""Timing II"""
def main(seconds):
    '''Variable'''
    if seconds < 0:
        print("ERR_:__:__:__")
        return
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if days > 9999:
        print("ERR_:__:__:__")
    else:
        print(f"{days:04}:{hours:02}:{minutes:02}:{seconds:02}")
main(seconds = int(input()))
