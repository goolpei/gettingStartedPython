import time
i: int = 0
st = time.perf_counter()
for _ in range(100000000):
    i += 1
et = time.perf_counter()
print(i)
print(et - st)