#hour: sec div 3600
#minute: (sec - hour*3600) div 60
#ss: sec mod 60

def readable_time(sec_only):
    hour = sec_only // 3600
    minute = (sec_only - hour * 3600) // 60
    ss = sec_only % 60
    return f"{hour:02d}:{minute:02d}:{ss:02d}"

print(readable_time(5601))

#one-line-boi

def readable_time2(s):
    return "{:02d}:{:02d}:{:02d}".format(s // 3600, s // 60 % 60, s % 60)

print(readable_time2(5601))