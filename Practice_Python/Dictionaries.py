# counts = {}

# counts['A'] = 1
# counts["B"] = 'd'

# print(counts.keys())
# print(counts.values())

# counts['A'] += 1
# print(counts.values())

# if 'C' in counts:
#     print(counts['C'])
# else: 
#     print("No key")

# game_map = {}

# game_map[(1, 2)] = 'starting point'
# game_map[(5, 5)] = 'save point' 
# game_map[(10, 11)] = 'end point' 

# current_pos = (5, 5)
# if current_pos in game_map:
#     print(f'You are currently in {game_map[current_pos]}.')

items = ['book', 'pencil', 'paper']
d = {}
for i, item in enumerate(items, start=1):
    d[i] = item

for index, object in d.items():
    print(f'Index {index} contains: {object}')

