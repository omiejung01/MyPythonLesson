import random

#Different probabilities and Time-in Time-out Threshold
def my_scenario():
    # scenario_a = 15%
    # scenario_b = 25%
    # scenario_c = 40%
    # scenario_d = 30%

    condition = random.randint(1,20)

    if condition in [1,2,3]:
        return 'a'
    elif condition in [4,5,6,7,8]:
        return 'b'
    elif condition in [9,10,11,12,13,14,15,16]:
        return 'c'
    else:
        return 'd'

def random_with_prob():
    #generate result 10,000 time and count
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0

    for x in range(0,10000):
        result = my_scenario()
        if result == 'a':
            count_a += 1
        elif result == 'b':
            count_b += 1
        elif result == 'c':
            count_c += 1
        else:
            count_d += 1

    print('a: ' + str(count_a))
    print('b: ' + str(count_b))
    print('c: ' + str(count_c))
    print('d: ' + str(count_d))

def working_hour(time_in, time_out):
    #  Format xx:xx
    #1 Time-in cut-off 15-minute after
    #2 Time-out cut-off 15-minute before
    #3 Error if time-out before or equal time-in

    in_hour = int(time_in[0:2])
    in_minute = int(time_in[3:5])
    if in_minute <= 15:
        in_minute = 15
    elif in_minute <= 30:
        in_minute = 30
    elif in_minute <= 45:
        in_minute = 45
    else:
        in_minute = 0
        in_hour += 1

    print(in_hour)
    print(in_minute)

    out_hour = int(time_out[0:2])
    out_minute = int(time_out[3:5])
    if out_minute <= 15:
        out_minute = 0
    elif out_minute <= 30:
        out_minute = 15
    elif out_minute <= 45:
        out_minute = 30
    else:
        out_minute = 45

    print(out_hour)
    print(out_minute)

    duration_minute = ((out_hour * 60) + out_minute) - ((in_hour * 60) + in_minute)

    if duration_minute <= 0:
        return 'Error!!'

    str_hour = str(duration_minute // 60) + ' hour(s)'
    if duration_minute < 60:
        str_hour = ''

    str_minute = str(duration_minute - (duration_minute // 60)*60) + ' minute(s)'
    if duration_minute - (duration_minute // 60) == 0:
        str_minute =''

    return str_hour + ' ' + str_minute


def timein_timeout():
    print(working_hour('17:11','16:47'))

if __name__ == '__main__':
    random_with_prob()
    timein_timeout()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
