def add_time(start, duration, week_day=None):
    new_time = None

    initial_am_pm = start[-1:-3:-1][::-1]

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    x = len(start)

    start_time = start[:x - 3].split(':')

    start_hour = int(start_time[0])
    start_min = int(start_time[1])

    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_min = int(duration_time[1])

    result_min = start_min + duration_min
    hours_2_add = 0
    remaining_min = result_min
    if result_min > 59:
        hours_2_add = result_min // 60
        remaining_min = result_min % 60
    if remaining_min < 10:
        remaining_min = '0' + str(remaining_min)

    days_2_add = duration_hour // 24
    remaining_duration_hours = duration_hour % 24

    result_hours = start_hour + remaining_duration_hours + hours_2_add
    how_many_days = None

    if result_hours < 12:
        new_time = str(result_hours) + ':' + str(remaining_min)

    elif result_hours == 12:
        new_time = str(result_hours) + ':' + str(remaining_min)

    elif result_hours > 12:
        remaining_hours = 12 if result_hours % 12 == 0 else result_hours % 12
        new_time = str(remaining_hours) + ':' + str(remaining_min)

    am_pm = initial_am_pm
    if result_hours >= 12:
        am_pm = 'AM' if initial_am_pm == 'PM' else 'PM'

    if am_pm == 'AM' and am_pm != initial_am_pm:
        days_2_add +=1
# add AM or PM to the calculated new time
    new_time += ' ' + am_pm

# if the week day is passed as argument
    if week_day is not None:
        i = days.index(week_day.capitalize())
        i += days_2_add
        i %= 7
        new_week_day = days[i]
        new_time += ', ' + new_week_day

    if days_2_add == 1:
        how_many_days = '(next day)'
    else:
        how_many_days = '(' + str(days_2_add) + ' days later)'

    if how_many_days is not None and days_2_add > 0:
        new_time += ' ' + how_many_days

    return new_time
