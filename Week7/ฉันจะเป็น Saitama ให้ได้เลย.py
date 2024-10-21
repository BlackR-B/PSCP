"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """main ฉันจะเป็น Saitama ให้ได้เลย"""
    push_up_goal = int(input())
    sit_up_goal = int(input())
    squat_goal = int(input())
    run_goal = int(input())
    push_up_per_day = int(input())
    sit_up_per_day = int(input())
    run_per_day = int(input())
    squat_per_day = int(input())
    days_push_up = math.ceil(push_up_goal / push_up_per_day)
    days_sit_up = math.ceil(sit_up_goal / sit_up_per_day)
    days_run = math.ceil(run_goal / run_per_day)
    days_squat = math.ceil(squat_goal / squat_per_day)
    days = days_push_up
    if days_sit_up > days:
        days = days_sit_up
    if days_run > days:
        days = days_run
    if days_squat > days:
        days = days_squat
    print(days)
main()
