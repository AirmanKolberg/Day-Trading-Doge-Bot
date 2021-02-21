from datetime import datetime
from time import sleep


def verify_int(var_in_question):
    if var_in_question % 1 == 0:
        return True
    else:
        return False


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def determine_if_market_open():
    day_of_week = datetime.today().strftime('%A')
    if day_of_week == 'Saturday' or day_of_week == 'Sunday':
        return False

    market_open = False
    while not market_open:
        the_time_now = get_current_time()
        the_hour = int(the_time_now[0:2])
        the_minute = int(the_time_now[3:5])
        the_second = int(the_time_now[6:9])

        if the_hour == 7:
            if the_minute >= 30:
                market_open = True
            else:
                minutes_remaining = 30 - the_minute
                seconds_remaining = 60 - the_second
                total_secs_to_go = (minutes_remaining * 60) + seconds_remaining
                print(f'The market will be open in {total_secs_to_go} seconds from now ({the_time_now}).')
                # sleep(total_secs_to_go)
        elif the_hour > 7:
            if the_hour >= 14:
                return False
            else:
                market_open = True
        else:
            hours_remaining = 7 - the_hour
            minutes_remaining = 30 - the_minute
            seconds_remaining = 60 - the_second
            total_secs_to_go = (hours_remaining * 3600) + (minutes_remaining * 60) + seconds_remaining
            print(f'The market will be open in {total_secs_to_go} seconds from now ({the_time_now}).')
            # sleep(total_secs_to_go)
        sleep(1)

    return True
