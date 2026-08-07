import random
import time
import copy


# --- 1. Your Custom Sort ---
def custom_gnubble_sort(arr):
    n = len(arr) - 1
    i = 0  # sorted boundary pointer

    def check_neighbors(arr, index):
        if index == 0:
            return arr[index] <= arr[index + 1]
        elif index == n:
            return arr[index] >= arr[index - 1]
        else:
            return arr[index - 1] <= arr[index] <= arr[index + 1]

    while i < n:
        j = i  # current pointer
        while True:
            if j == 0:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                else:
                    break
            elif j == n:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                else:
                    break
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                elif arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                else:
                    break

        if check_neighbors(arr, i):
            i += 1


# --- 2. Standard Bubble Sort ---
def standard_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# --- 3. Benchmarking Suite ---
def benchmark_sorting_algorithms(sizes, trials=5):
    print(f"{'List Size':<12} | {'Custom Sort (s)':<18} | {'Bubble Sort (s)':<18} | {'Ratio (Custom/Bubble)':<20}")
    print("-" * 75)

    for size in sizes:
        custom_total_time = 0.0
        bubble_total_time = 0.0

        for _ in range(trials):
            # Generate a random test list
            original_list = [random.randint(0, 10000) for _ in range(size)]

            # Copy list so both algorithms start with identical inputs
            list_for_custom = copy.deepcopy(original_list)
            list_for_bubble = copy.deepcopy(original_list)

            # Benchmark Custom Sort
            start_time = time.perf_counter()
            custom_gnubble_sort(list_for_custom)
            custom_total_time += time.perf_counter() - start_time

            # Benchmark Bubble Sort
            start_time = time.perf_counter()
            standard_bubble_sort(list_for_bubble)
            bubble_total_time += time.perf_counter() - start_time

        # Calculate average runtime across trials
        avg_custom = custom_total_time / trials
        avg_bubble = bubble_total_time / trials
        ratio = avg_custom / avg_bubble if avg_bubble > 0 else 0

        print(f"{size:<12} | {avg_custom:<18.5f} | {avg_bubble:<18.5f} | {ratio:<20.2f}x")


# Run the benchmark on varying list sizes
if __name__ == "__main__":
    # Keeping sizes under 1500 elements since both algorithms are O(n^2)
    test_sizes = [100, 250, 500, 750, 1000]
    benchmark_sorting_algorithms(test_sizes, trials=3)