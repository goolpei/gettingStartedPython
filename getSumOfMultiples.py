def get_sum_of_multiples(multiples, nth_sum):

    return sum(x for x in range(1, nth_sum + 1) if x % multiples[0] == 0 or x % multiples[1] == 0)

print(get_sum_of_multiples([3, 5], 999))