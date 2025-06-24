import math

def is_armstrong(n):
    """
    Check if a number is an Armstrong (Narcissistic) number.
    A number is Armstrong if the sum of its digits raised to the number of digits equals the original number.
    """
    temp = n
    res = 0
    digits = count_digits(n)

    while temp > 0:
        dig = temp % 10
        res += (dig ** digits)
        temp //= 10

    return res == n

def count_digits(n):
    """
    Count number of digits in an integer using math.
    Returns 1 for number 0.
    """
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1

# Safe test execution
if __name__ == "__main__":
    test_number = 9474
    print(f"Is {test_number} an Armstrong number? {is_armstrong(test_number)}")
    print(f"Number of digits in {test_number}: {count_digits(test_number)}")
