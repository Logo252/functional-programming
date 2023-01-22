import time

NUMBERS = [40, 41]


def calculate_fibonacci(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
    return x


if __name__ == "__main__":
    start_time = time.time()

    for number in NUMBERS:
        factorial = calculate_fibonacci(number)
        print(f"Fibonacci of {number}: {factorial}")

    duration_in_ms = (time.time() - start_time) * 1000
    print("-------------------")
    print(f"Finished in {duration_in_ms} milli seconds")
