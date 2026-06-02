def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def main():
    print("Average Calculator")

    count = int(input("How many numbers? "))

    nums = []
    for i in range(count):
        value = int(input(f"Enter number {i + 1}: "))
        nums.append(value)

    avg = average(nums)
    print("Average:", avg)


main()
