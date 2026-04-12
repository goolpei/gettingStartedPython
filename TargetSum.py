
print('Enter an array of numbers:', end=' ')
arr = list(map(int, input().split()))
target_sum = int(input('Enter target sum: '))

arr.sort()

left = 0
right = len(arr) - 1
found = False

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target_sum:
        found = True
        print(f'{arr[left]} + {arr[right]} = {target_sum}')
        break
    elif current_sum > target_sum:
        right -= 1
    else:
        left += 1

if not found:
    print('No sum found.')


