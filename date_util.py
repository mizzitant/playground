import datetime as dt
import time


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

#start = datetime.time(23, 0, 0)
start = dt.datetime.strptime('23:00:00', '%H:%M:%S').time()
start_dt = dt.datetime.strptime('23:00:00', '%H:%M:%S')
dur_dt = dt.datetime.strptime('00:05:00', '%H:%M:%S')
dur = dt.timedelta(hours=dur_dt.hour, minutes=dur_dt.minute, seconds=dur_dt.second)
end_dt = start_dt + dur
end1_dt = dt.datetime.combine(dt.date.today(), start) + dur

print(start)
print(end_dt.time())
print(dt.datetime.now().time())

print(time_in_range(start, end_dt.time(), dt.datetime.now().time()))
print(time_in_range(start_dt, end1_dt, dt.datetime.now()))  # doesn't work
print(time_in_range(start_dt, end1_dt, dt.datetime.combine(dt.date.today(), dt.time(23, 30, 0))))
print(time_in_range(start, end_dt.time(), dt.time(12, 30, 0)))
