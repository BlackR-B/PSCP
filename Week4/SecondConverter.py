"""SecondConverter"""
def convert_seconds_to_time(k, s, m, h):
    """main"""
    seconds_per_minute = s
    seconds_per_hour = seconds_per_minute * m
    seconds_per_day = seconds_per_hour * h
    seconds_today = k % seconds_per_day
    hours = seconds_today // seconds_per_hour
    seconds_today %= seconds_per_hour
    minutes = seconds_today // seconds_per_minute
    seconds = seconds_today % seconds_per_minute
    print(f"{hours}:{minutes}:{seconds}")
convert_seconds_to_time(int(input()), int(input()), int(input()), int(input()))
