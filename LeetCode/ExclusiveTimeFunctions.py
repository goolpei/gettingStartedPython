from typing import List
# two-pointer method, distances between logs

def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    # start is inclusive, end is inclusive
    exclusive_time = [0 for _ in range(n)]
    # ["0:start:0","1:start:2","1:end:5","0:end:6"]
    # ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    # ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    
    stack = []
    prev_time = 0
    for log in logs:

        func_id, state, timestamp = log.split(':')
        func_id = int(func_id)
        timestamp = int(timestamp)

        if state == 'start':

            if not stack:
                stack.append(func_id)
                prev_time = timestamp
            else:
                exclusive_time[stack[-1]] += (timestamp - prev_time)
                stack.append(func_id)
                prev_time = timestamp

        if state == 'end':
            pop_func_id = stack.pop()
            exclusive_time[pop_func_id] += (timestamp - prev_time + 1)
            prev_time = timestamp + 1

    return exclusive_time