def race(v1, v2, lead):
    if v1 >= v2: return None
    # [hour, min, sec]
    time_taken = lead / (v2 - v1)
    hour = int(time_taken)
    min = (time_taken - hour) * 60
    minute = round(min)
    sec = (min - minute) * 60
    second = round(sec)
    return [[hour, minute, second]]
    
    
def race2(v1, v2, lead):
    if v1 >= v2: 
        return None
        
    # 1. Calculate total seconds using integer division (//)
    # Time = Lead / Delta_Velocity. To get seconds, multiply by 3600 first.
    total_seconds = (lead * 3600) // (v2 - v1)
    
    # 2. Break down total seconds into hours, minutes, and seconds
    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60
    
    return [hour, minute, second]

print(race2(820, 850, 550))