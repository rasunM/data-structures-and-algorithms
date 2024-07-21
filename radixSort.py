from functools import reduce

def radix_sort(numbers, num_digits):
    """Sorts a list of numbers using the Radix Sort algorithm.

    Args:
        numbers (list): The list of integers to sort.
        num_digits (int): The number of digits in the largest number.

    Returns:
        list: The sorted list of integers.
    """
    for digit in range(num_digits):
        buckets = [[] for _ in range(10)]
        for number in numbers:
            bucket_index = (number // 10 ** digit) % 10
            buckets[bucket_index].append(number) #append the number into the relavent bucket
        numbers = reduce(lambda x, y: x + y, buckets) #flatted the buckets into a single list
        print(numbers)
    return numbers

def main():
    numbers = [205, 101, 4, 89, 23, 456, 74, 1, 2, 45, 3, 562, 77]
    num_digits = len(str(max(numbers)))
    sorted_numbers = radix_sort(numbers, num_digits)
    print("Sorted List:", sorted_numbers)

if __name__ == "__main__":
    main()
