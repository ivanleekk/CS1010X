import math

def time_difference(time1, time2):
    time1_seconds = time_to_seconds(time1)
    time2_seconds = time_to_seconds(time2)
    time_diff = time2_seconds - time1_seconds
    return make_time_string(math.floor(time_diff / 3600),math.floor(time_diff/60)-math.floor(time_diff / 3600)*60,time_diff%60)
    pass
    
    
# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)

print(time_difference('01:02:03', '13:12:11'))
print(time_difference('11:46:39', '22:31:17'))
print(time_difference('00:00:00', '23:59:59'))
print(time_difference('00:00:00', '00:00:01'))
