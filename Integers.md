<<<<<<< HEAD
# **`Integers`**

## ✅ 1. Armstrong Number (Narcissistic Number)

#### ❓What is an Armstrong Number?
An **Armstrong number** (also called a **narcissistic number**) is a number that is equal to the **sum of its own digits each raised to the power of the number of digits**.

#### 🔢 Mathematical Explanation:
For a number `n`, with `d` digits:  
If  
```
(sum of each digit ** d) == original number  
```
Then it is an Armstrong number.

##### For example:
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = **153** ✅  
- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = **9474** ✅  
- 143 = 1³ + 4³ + 3³ = 1 + 64 + 27 = **92** ❌ (Not an Armstrong number)

---

#### 💡 Python Implementation – Using Iteration:

```python
def is_armstrong(n):
    temp = n                   # Keep original number
    res = 0                    # Result accumulator
    digits = len(str(n))       # Count of digits

    while temp > 0:
        dig = temp % 10        # Get last digit
        res += dig ** digits   # Add digit raised to power of count
        temp //= 10            # Remove last digit

    return res == n            # Return True if condition matches

print(is_armstrong(153))  # True
print(is_armstrong(143))  # False
```

---

#### 🧠 Alternate Approach:
Using list comprehension and `sum()`:

```python
def is_armstrong(n):
    return n == sum(int(digit)**len(str(n)) for digit in str(n))
```

---

#### 🔍 Real-World Analogy:
Armstrong numbers are mostly for mathematical curiosity, but the concept is often introduced in early programming to practice digit manipulation and loops.

---

---

## ✅ 2. Palindrome Number

---

### ❓What is a Palindrome Number?

A **palindrome number** is a number that **remains the same when its digits are reversed**.

#### 🔢 Mathematical Explanation:
A number `n` is called a **palindrome** if:
```
reverse(n) == n
```

---

### 🔁 Example Series:
- 121 → Reverse is 121 → ✅ Palindrome  
- 12321 → Reverse is 12321 → ✅ Palindrome  
- 123 → Reverse is 321 → ❌ Not a Palindrome  
- 345463 → Reverse is 364543 → ❌ Not a Palindrome

---

### 🎯 Objective:
Given an integer, check whether it is a palindrome number or not without converting it into a string.

---

### ✅ Method 1: Using Simple Iteration (while loop)

```python
def is_digit_palindrome(n):
    temp = n               # Store original value
    rev = 0                # Reverse number

    while temp > 0:
        dig = temp % 10    # Get last digit
        rev = dig + rev * 10  # Append digit to reverse
        temp = temp // 10  # Remove last digit

    return rev == n        # Compare reversed with original

print(is_digit_palindrome(12321))  # True
print(is_digit_palindrome(123))    # False
```

---

### ✅ Method 2: Using String Reversal (Pythonic)

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(12321))  # True
print(is_palindrome(123))    # False
```

---

### 🧠 Real-World Analogy:
- Palindromes are used in **data validation**, **security patterns**, and even **DNA pattern recognition** in bioinformatics.
- Common examples: Racecar, 12321, "madam", etc.

---

### ✅ Summary:
| Feature             | Description                         |
|---------------------|-------------------------------------|
| Concept             | Reversing a number and comparing    |
| Edge Cases          | 0 is a palindrome                   |
| Don't use string?   | Use while loop + `%` and `//`       |
| Can use string?     | Simple Pythonic one-liner           |

---


---

## ✅ 3. Digit Sum

---

### ❓What is Digit Sum?

The **digit sum** of a number is the **sum of all its individual digits**.  
This operation is widely used in checksum calculations, digital roots, etc.

---

### 🔢 Mathematical Explanation:

For a number `n = 1234`,  
Digit Sum = 1 + 2 + 3 + 4 = **10**

---

### 🧪 Example Inputs & Outputs:

- 123 → 1 + 2 + 3 = 6  
- 105 → 1 + 0 + 5 = 6  
- 9999 → 9 + 9 + 9 + 9 = 36

---

### ✅ Method 1: Iterative Method without String Conversion

```python
def digit_sum(n):
    if n <= 0:
        return 'number must be greater than 0'

    total = 0
    while n > 0:
        digit = n % 10          # Extract last digit
        total += digit          # Add to sum
        n //= 10                # Remove last digit
    return total

print(digit_sum(1234))  # Output: 10
```

---

### ✅ Method 2: Using String Conversion (Pythonic Way)

```python
def digit_sum(n):
    return sum(int(d) for d in str(n))

print(digit_sum(105))  # Output: 6
```

---

### ✅ Method 3: Recursive Approach

```python
def digit_sum_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum_recursive(n // 10)

print(digit_sum_recursive(123))  # Output: 6
```

---

### 🧠 Real-World Usage:
- Used in **credit card checksum** (Luhn algorithm).
- Helps in **digital root** or **casting out nines** in math checks.

---

## ✅ 4. Count Digits in a Number

---

### ❓What is Digit Count?

**Digit count** tells how many digits a number contains.

---

### 🔢 Mathematical Explanation:

Number of digits in `n` = floor(log₁₀(n)) + 1  
*(Only if n > 0)*

---

### 🧪 Examples:
- 123 → 3 digits  
- 1001 → 4 digits  
- 0 → 1 digit (edge case)

---

### ✅ Method 1: Iterative Loop (without converting to string)

```python
def digit_count(n):
    if n <= 0:
        return 'number must be greater than 0'
    
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(digit_count(234567))  # Output: 6
```

---

### ✅ Method 2: Using Logarithmic Function

```python
import math

def digit_count_math(n):
    if n > 0:
        return math.floor(math.log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return 'number must be non-negative'

print(digit_count_math(1001))  # Output: 4
```

---

### ✅ Method 3: Using String Length

```python
def digit_count_str(n):
    return len(str(abs(n))) if n >= 0 else 'number must be non-negative'

print(digit_count_str(0))  # Output: 1
```

---

## ✅ 5. Count Zeros in a Number

---

### ❓What is Zero Count?

Count how many **0 digits** exist in a number.

---

### 🔢 Examples:
- 102030 → 3 zeros  
- 1000 → 3 zeros  
- 1234 → 0 zeros  
- 0 → 1 zero (edge case)

---

### ✅ Method 1: Using String Conversion

```python
def cnt_zeros_str(n):
    count = 0
    for digit in str(n):
        if int(digit) == 0:
            count += 1
    return count

print(cnt_zeros_str(1020300))  # Output: 4
```

---

### ✅ Method 2: Without Using String (Pure Integer)

```python
def count_zeros(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    count = 0
    while n > 0:
        if n % 10 == 0:
            count += 1
        n //= 10
    return count

print(count_zeros(1020300))  # Output: 4
```

---

## ✅ 6. Anagram Numbers (Digit Anagram)

---

### ❓What is an Anagram Number?

Two numbers are **digit anagrams** if they have:
- Same digits
- Same frequency
- But possibly in different order

---

### 🔢 Examples:

- 3456 and 6543 → ✅ Anagram  
- 1122 and 2211 → ✅ Anagram  
- 123 and 3210 → ❌ Not Anagram (different digits)

---

### ✅ Method 1: Using Frequency Array (0–9 digits)

```python
def anagram(n):
    freq = [0]*10
    while n > 0:
        dig = n % 10
        freq[dig] += 1
        n //= 10
    return freq

def anagram_digits(n1, n2):
    return anagram(n1) == anagram(n2)

print(anagram_digits(3456, 6345))  # Output: True
print(anagram_digits(3456, 6340))  # Output: False
```

---

### ✅ Method 2: Using `collections.Counter` (string-based)

```python
from collections import Counter

def anagram_digits(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))

print(anagram_digits(1233, 3321))  # Output: True
```

---

### 🧠 Real-World Analogy:
- Digit anagrams resemble **anagram words**: 'listen' & 'silent'
- Useful in **pattern-matching**, **data deduplication**, **puzzles**, etc.

---

### ✅ Summary Table

| Concept        | Core Idea                            | Efficient Tip                     |
|----------------|---------------------------------------|-----------------------------------|
| Digit Sum      | Sum of all digits                    | Use `%` and `//` or `sum(str())` |
| Count Digits   | How many digits                      | Use loop, `len(str())`, or `log` |
| Count Zeros    | Count of digit `0` in a number        | Loop using `%10` or `str().count()` |
| Anagram Number | Same digits, same frequency           | Use digit-frequency or `Counter` |


---

---

## ✅ 7. Factorial of a Number

---

### ❓What is Factorial?

The **factorial** of a number `n` (denoted `n!`) is the **product of all positive integers** less than or equal to `n`.

---

### 🔢 Mathematical Explanation:

- `n! = n × (n-1) × (n-2) × ... × 2 × 1`
- `0! = 1` (by definition)

---

### 🧪 Example Inputs & Outputs:

- `5! = 5×4×3×2×1 = 120`  
- `3! = 3×2×1 = 6`  
- `0! = 1`  
- `1! = 1`

---

### ✅ Method 1: Iterative Approach

```python
def fact_num(n):
    if n <= 1:
        return 1
    fact = 1
    for num in range(1, n+1):
        fact *= num
    return fact

print(fact_num(5))  # Output: 120
```

---

### ✅ Method 2: Using Recursion

```python
def fact_recursive(n):
    if n <= 1:
        return 1
    return n * fact_recursive(n-1)

print(fact_recursive(5))  # Output: 120
```

---

### ✅ Method 3: Using `math` Module

```python
import math

def facto(n):
    return math.factorial(n)

print(facto(5))  # Output: 120
```

---

### 🧠 Real-World Usage:

- **Permutations & combinations**
- **Probability theory**
- **Mathematical expressions** in calculus and algebra

---

## ✅ 8. Fibonacci Series  

---

### ❓What is the Fibonacci Series?

The Fibonacci Series is a unique sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

---

### 🔢 Mathematical Explanation:

In mathematical terms, the series is defined by the recurrence relation:

```
F(n) = F(n-1) + F(n-2)
```

Where:
- F(0) = 0  
- F(1) = 1

So the series begins as:  
`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`

---

### 📌 Objective:

Given an integer input `n`, find and return the Fibonacci Series up to the Nth term using different methods.

---

### ✅ Method 1: Using Simple Iteration (Loop-based)

```python
def fib_seq(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fib_seq(10)  # Output: 0 1 1 2 3 5 8 13 21 34
```

#### 📘 Explanation:

- Start with `a = 0` and `b = 1`
- Loop `n` times, printing the current value of `a`
- Update `a` and `b` to next Fibonacci pair

---

### ✅ Method 2: Recursive Function

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

for i in range(10):
    print(fib_recursive(i), end=' ')
```

#### 📘 Explanation:

- A direct recursive implementation of the formula
- Very readable, but **inefficient** due to repeated calls

---

### ✅ Method 3: Return Series as a List (Efficient)

```python
def fib_list(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib_list(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### ✅ Method 4: Using Direct Formula (Binet's Formula – Not Always Precise for Large n)

```python
import math

def fib_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-1/phi)**n) / math.sqrt(5))

for i in range(10):
    print(fib_formula(i), end=' ')
```

#### 📘 Note:
May produce floating point inaccuracies for large `n`.

---

### 🧠 Real-World Usage:

- Fibonacci numbers appear in **nature** (petal counts, spiral shells)
- Used in **computer algorithms** (e.g., dynamic programming)
- Also found in **stock market analysis**, **game development**, and **combinatorics**

---

### ✅ Summary Table

| Method            | Description              | Performance       |
|-------------------|--------------------------|-------------------|
| Iterative Loop    | Simple and fast          | ✅ Efficient       |
| Recursion         | Clean but slow           | ❌ Inefficient     |
| Return List       | Stores series as list    | ✅ Good for reuse  |
| Binet’s Formula   | Quick direct math formula| ❌ Slight error    |
```
---

## ✅ 9. Happy Number

---

### ❓What is a Happy Number?

A number is called **happy** if by **repeatedly replacing the number with the sum of squares of its digits**, you eventually get `1`.

If it falls into a cycle and never reaches `1`, it's **not** a happy number.

---

### 🔢 Example:

- 19 →  
  1² + 9² = 82  
  8² + 2² = 68  
  6² + 8² = 100  
  1² + 0² + 0² = 1 ✅

- 4 →  
  4² = 16  
  1² + 6² = 37  
  3² + 7² = 58  
  5² + 8² = 89  
  …loops forever ❌

---

### ✅ Method: Loop with Set to Detect Cycles

```python
def is_happy_number(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        n = total
    return True

print(is_happy_number(19))  # True
print(is_happy_number(4))   # False
```

---

### 🧠 Real-World Use:

- Teaching concepts of **cycle detection**
- Applied in puzzles and mathematical curiosity

---

## ✅ 10. Prime Number Check

---

### ❓What is a Prime Number?

A number that is **greater than 1** and has **no divisors other than 1 and itself**.

---

### 🔢 Examples:

- 2 → ✅ Prime (smallest even prime)  
- 3 → ✅ Prime  
- 4 → ❌ Not Prime  
- 17 → ✅ Prime

---

### ✅ Method 1: Brute Force

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
```

---

### ✅ Method 2: Optimized up to √n

```python
def is_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

---

### 🧠 Real-World Usage:

- **Cryptography**
- **Random number generators**
- Used in **hashing & compression**

---

## ✅ 11. Prime Numbers in a Range

---

### ❓Objective:
Generate all prime numbers between two values `x` and `y`.

---

### ✅ Method: Use Loop with Prime Check Inside

```python
def prime_range(x, y):
    if x <= 1:
        x = 2
    primes = []

    for i in range(x, y+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(prime_range(4, 20))  # Output: [5, 7, 11, 13, 17, 19]
```

---

### 🔍 for-else Note:
The `else` block runs **only if loop is not broken**, hence it's used to detect primes.

---

## ✅ 12. Reverse Digits of a Number

---

### ❓What is Reverse of Digits?

Reverse a number without converting to string.

---

### 🔢 Examples:

- 123 → 321  
- 1001 → 1001  
- 0 → 0

---

### ✅ Method: Digit Manipulation Using While Loop

```python
def rev_digits(n):
    if n <= 0:
        return 'number must be greater than 0'

    rev = 0
    while n > 0:
        dig = n % 10
        rev = dig + rev * 10
        n //= 10
    return rev

print(rev_digits(34567))  # Output: 76543
```

---

## ✅ 13. Square Root of a Number

---

### ❓What is Square Root?

A number `x` is a **square root** of `n` if `x*x == n`.  
We may return the **floor value** if `n` is not a perfect square.

---

### ✅ Method 1: Using Built-in `math.sqrt()`

```python
import math

def sq_root(n):
    return math.sqrt(n)

print(sq_root(49))  # Output: 7.0
```

---

### ✅ Method 2: Using `** 0.5` Operator

```python
def sq_pow(n):
    return n ** 0.5

print(sq_pow(16))  # Output: 4.0
```

---

### ✅ Method 3: Binary Search (Divide and Conquer)

```python
def sqrt_dc(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n

    low = 0
    high = n
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

print(sqrt_dc(35))  # Output: 5
```

---

### 🧠 Real-World Use:

- **Root calculations** in math & physics
- **Game mechanics**, distances, or movement logic

---

### ✅ Summary Table for 7–15

| Concept            | Use/Definition                             | Efficient Way                     |
|--------------------|---------------------------------------------|-----------------------------------|
| Factorial          | Product of integers till `n`                | Use `math.factorial()` or loop   |
| Happy Number       | Sum of squares of digits → ends in 1        | Use set to detect cycles         |
| Prime Number       | Only divisible by 1 and itself              | Check till √n                    |
| Prime in Range     | Find all primes between `x` and `y`         | Use inner loop with break/else   |
| Reverse Digits     | Reverse number (e.g., 123 → 321)            | `%10`, `rev = dig + rev*10`      |
| Square Root        | Return √n (floor if not perfect)            | Use binary search for large `n`  |

---


---

## ✅ 16. Strong Number

---

### ❓What is a Strong Number?

A **strong number** is a number in which the **sum of the factorial of each digit** is equal to the original number.

---

### 🔢 Mathematical Explanation:

If  
```
sum(fact(digit)) == number
```
then it is a Strong Number.

---

### 🧪 Examples:

- 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅  
- 2 → 2! = 2 ✅  
- 123 → 1! + 2! + 3! = 9 ❌

---

### ✅ Python Code:

```python
import math

def is_strong(n):
    temp = n
    result = 0
    while temp > 0:
        digit = temp % 10
        result += math.factorial(digit)
        temp //= 10
    return result == n

print(is_strong(145))  # Output: True
```

---

## ✅ 17. Disarium Number

---

### ❓What is a Disarium Number?

A number is **Disarium** if the **sum of its digits powered with their respective positions** is equal to the number.

---

### 🔢 Mathematical Explanation:

If `n = 135`, then  
1¹ + 3² + 5³ = 1 + 9 + 125 = **135** ✅

---

### ✅ Python Code:

```python
def is_disarium(n):
    digits = list(map(int, str(n)))
    return sum(d ** (i + 1) for i, d in enumerate(digits)) == n

print(is_disarium(135))  # Output: True
```

---

## ✅ 18. Harshad Number (Niven Number)

---

### ❓What is a Harshad Number?

A number is called **Harshad** if it is **divisible by the sum of its digits**.

---

### 🔢 Examples:

- 18 → 1+8 = 9, 18 % 9 == 0 ✅  
- 21 → 2+1 = 3, 21 % 3 == 0 ✅  
- 19 → 1+9 = 10, 19 % 10 ❌

---

### ✅ Python Code:

```python
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

print(is_harshad(18))  # Output: True
```

---

## ✅ 19. Automorphic Number (Curious Number)

---

### ❓What is an Automorphic Number?

A number is called **automorphic** if its **square ends with the number itself**.

---

### 🔢 Examples:

- 5² = 25 → ends in 5 ✅  
- 76² = 5776 → ends in 76 ✅  
- 7² = 49 → ❌

---

### ✅ Python Code:

```python
def is_automorphic(n):
    return str(n * n).endswith(str(n))

print(is_automorphic(76))  # Output: True
```

---

## ✅ 20. Neon Number

---

### ❓What is a Neon Number?

A **neon number** is a number where the **sum of digits of its square equals the number itself**.

---

### 🔢 Examples:

- 9² = 81 → 8+1 = 9 ✅  
- 1² = 1 → ✅  
- 7² = 49 → 4+9 = 13 ❌

---

### ✅ Python Code:

```python
def is_neon(n):
    return sum(int(d) for d in str(n * n)) == n

print(is_neon(9))  # Output: True
```

---

## ✅ 21. Krishnamurthy Number (Also Strong Number)

**Already covered as Strong Number above.**

---

## ✅ 22. Digital Root

---

### ❓What is a Digital Root?

The **repeated sum of digits** until you get a single-digit number.

---

### 🔢 Examples:

- 456 → 4+5+6 = 15 → 1+5 = **6**  
- 9999 → 9+9+9+9 = 36 → 3+6 = **9**

---

### ✅ Method 1: Loop-based

```python
def digital_root(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

print(digital_root(456))  # Output: 6
```

---

## ✅ 23. Power of Two

---

### ❓What is a Power of 2?

If a number can be expressed as `2^k`, then it is a **power of two**.

---

### 🔢 Examples:

- 8 = 2³ ✅  
- 16 = 2⁴ ✅  
- 10 ❌

---

### ✅ Python Code:

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # Output: True
```

---

## ✅ 24. Armstrong Numbers in a Range

**Already explained under Armstrong, now range form:**

```python
def armstrong_range(x, y):
    result = []
    for n in range(x, y+1):
        digits = len(str(n))
        if n == sum(int(d)**digits for d in str(n)):
            result.append(n)
    return result

print(armstrong_range(100, 999))  # Output: [153, 370, 371, 407]
```

---

## ✅ 25. Magic Number

---

### ❓What is a Magic Number?

A number is called **magic** if **repeated digit sum == 1**.

---

### 🔢 Examples:

- 1729 → 1+7+2+9 = 19 → 1+9 = 10 → 1+0 = 1 ✅  
- 1234 → ❌

---

### ✅ Python Code:

```python
def is_magic(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n == 1

print(is_magic(1729))  # Output: True
```

=======
# **`Integers`**

## ✅ 1. Armstrong Number (Narcissistic Number)

#### ❓What is an Armstrong Number?
An **Armstrong number** (also called a **narcissistic number**) is a number that is equal to the **sum of its own digits each raised to the power of the number of digits**.

#### 🔢 Mathematical Explanation:
For a number `n`, with `d` digits:  
If  
```
(sum of each digit ** d) == original number  
```
Then it is an Armstrong number.

##### For example:
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = **153** ✅  
- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = **9474** ✅  
- 143 = 1³ + 4³ + 3³ = 1 + 64 + 27 = **92** ❌ (Not an Armstrong number)

---

#### 💡 Python Implementation – Using Iteration:

```python
def is_armstrong(n):
    temp = n                   # Keep original number
    res = 0                    # Result accumulator
    digits = len(str(n))       # Count of digits

    while temp > 0:
        dig = temp % 10        # Get last digit
        res += dig ** digits   # Add digit raised to power of count
        temp //= 10            # Remove last digit

    return res == n            # Return True if condition matches

print(is_armstrong(153))  # True
print(is_armstrong(143))  # False
```

---

#### 🧠 Alternate Approach:
Using list comprehension and `sum()`:

```python
def is_armstrong(n):
    return n == sum(int(digit)**len(str(n)) for digit in str(n))
```

---

#### 🔍 Real-World Analogy:
Armstrong numbers are mostly for mathematical curiosity, but the concept is often introduced in early programming to practice digit manipulation and loops.

---

---

## ✅ 2. Palindrome Number

---

### ❓What is a Palindrome Number?

A **palindrome number** is a number that **remains the same when its digits are reversed**.

#### 🔢 Mathematical Explanation:
A number `n` is called a **palindrome** if:
```
reverse(n) == n
```

---

### 🔁 Example Series:
- 121 → Reverse is 121 → ✅ Palindrome  
- 12321 → Reverse is 12321 → ✅ Palindrome  
- 123 → Reverse is 321 → ❌ Not a Palindrome  
- 345463 → Reverse is 364543 → ❌ Not a Palindrome

---

### 🎯 Objective:
Given an integer, check whether it is a palindrome number or not without converting it into a string.

---

### ✅ Method 1: Using Simple Iteration (while loop)

```python
def is_digit_palindrome(n):
    temp = n               # Store original value
    rev = 0                # Reverse number

    while temp > 0:
        dig = temp % 10    # Get last digit
        rev = dig + rev * 10  # Append digit to reverse
        temp = temp // 10  # Remove last digit

    return rev == n        # Compare reversed with original

print(is_digit_palindrome(12321))  # True
print(is_digit_palindrome(123))    # False
```

---

### ✅ Method 2: Using String Reversal (Pythonic)

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(12321))  # True
print(is_palindrome(123))    # False
```

---

### 🧠 Real-World Analogy:
- Palindromes are used in **data validation**, **security patterns**, and even **DNA pattern recognition** in bioinformatics.
- Common examples: Racecar, 12321, "madam", etc.

---

### ✅ Summary:
| Feature             | Description                         |
|---------------------|-------------------------------------|
| Concept             | Reversing a number and comparing    |
| Edge Cases          | 0 is a palindrome                   |
| Don't use string?   | Use while loop + `%` and `//`       |
| Can use string?     | Simple Pythonic one-liner           |

---


---

## ✅ 3. Digit Sum

---

### ❓What is Digit Sum?

The **digit sum** of a number is the **sum of all its individual digits**.  
This operation is widely used in checksum calculations, digital roots, etc.

---

### 🔢 Mathematical Explanation:

For a number `n = 1234`,  
Digit Sum = 1 + 2 + 3 + 4 = **10**

---

### 🧪 Example Inputs & Outputs:

- 123 → 1 + 2 + 3 = 6  
- 105 → 1 + 0 + 5 = 6  
- 9999 → 9 + 9 + 9 + 9 = 36

---

### ✅ Method 1: Iterative Method without String Conversion

```python
def digit_sum(n):
    if n <= 0:
        return 'number must be greater than 0'

    total = 0
    while n > 0:
        digit = n % 10          # Extract last digit
        total += digit          # Add to sum
        n //= 10                # Remove last digit
    return total

print(digit_sum(1234))  # Output: 10
```

---

### ✅ Method 2: Using String Conversion (Pythonic Way)

```python
def digit_sum(n):
    return sum(int(d) for d in str(n))

print(digit_sum(105))  # Output: 6
```

---

### ✅ Method 3: Recursive Approach

```python
def digit_sum_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum_recursive(n // 10)

print(digit_sum_recursive(123))  # Output: 6
```

---

### 🧠 Real-World Usage:
- Used in **credit card checksum** (Luhn algorithm).
- Helps in **digital root** or **casting out nines** in math checks.

---

## ✅ 4. Count Digits in a Number

---

### ❓What is Digit Count?

**Digit count** tells how many digits a number contains.

---

### 🔢 Mathematical Explanation:

Number of digits in `n` = floor(log₁₀(n)) + 1  
*(Only if n > 0)*

---

### 🧪 Examples:
- 123 → 3 digits  
- 1001 → 4 digits  
- 0 → 1 digit (edge case)

---

### ✅ Method 1: Iterative Loop (without converting to string)

```python
def digit_count(n):
    if n <= 0:
        return 'number must be greater than 0'
    
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(digit_count(234567))  # Output: 6
```

---

### ✅ Method 2: Using Logarithmic Function

```python
import math

def digit_count_math(n):
    if n > 0:
        return math.floor(math.log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return 'number must be non-negative'

print(digit_count_math(1001))  # Output: 4
```

---

### ✅ Method 3: Using String Length

```python
def digit_count_str(n):
    return len(str(abs(n))) if n >= 0 else 'number must be non-negative'

print(digit_count_str(0))  # Output: 1
```

---

## ✅ 5. Count Zeros in a Number

---

### ❓What is Zero Count?

Count how many **0 digits** exist in a number.

---

### 🔢 Examples:
- 102030 → 3 zeros  
- 1000 → 3 zeros  
- 1234 → 0 zeros  
- 0 → 1 zero (edge case)

---

### ✅ Method 1: Using String Conversion

```python
def cnt_zeros_str(n):
    count = 0
    for digit in str(n):
        if int(digit) == 0:
            count += 1
    return count

print(cnt_zeros_str(1020300))  # Output: 4
```

---

### ✅ Method 2: Without Using String (Pure Integer)

```python
def count_zeros(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    count = 0
    while n > 0:
        if n % 10 == 0:
            count += 1
        n //= 10
    return count

print(count_zeros(1020300))  # Output: 4
```

---

## ✅ 6. Anagram Numbers (Digit Anagram)

---

### ❓What is an Anagram Number?

Two numbers are **digit anagrams** if they have:
- Same digits
- Same frequency
- But possibly in different order

---

### 🔢 Examples:

- 3456 and 6543 → ✅ Anagram  
- 1122 and 2211 → ✅ Anagram  
- 123 and 3210 → ❌ Not Anagram (different digits)

---

### ✅ Method 1: Using Frequency Array (0–9 digits)

```python
def anagram(n):
    freq = [0]*10
    while n > 0:
        dig = n % 10
        freq[dig] += 1
        n //= 10
    return freq

def anagram_digits(n1, n2):
    return anagram(n1) == anagram(n2)

print(anagram_digits(3456, 6345))  # Output: True
print(anagram_digits(3456, 6340))  # Output: False
```

---

### ✅ Method 2: Using `collections.Counter` (string-based)

```python
from collections import Counter

def anagram_digits(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))

print(anagram_digits(1233, 3321))  # Output: True
```

---

### 🧠 Real-World Analogy:
- Digit anagrams resemble **anagram words**: 'listen' & 'silent'
- Useful in **pattern-matching**, **data deduplication**, **puzzles**, etc.

---

### ✅ Summary Table

| Concept        | Core Idea                            | Efficient Tip                     |
|----------------|---------------------------------------|-----------------------------------|
| Digit Sum      | Sum of all digits                    | Use `%` and `//` or `sum(str())` |
| Count Digits   | How many digits                      | Use loop, `len(str())`, or `log` |
| Count Zeros    | Count of digit `0` in a number        | Loop using `%10` or `str().count()` |
| Anagram Number | Same digits, same frequency           | Use digit-frequency or `Counter` |


---

---

## ✅ 7. Factorial of a Number

---

### ❓What is Factorial?

The **factorial** of a number `n` (denoted `n!`) is the **product of all positive integers** less than or equal to `n`.

---

### 🔢 Mathematical Explanation:

- `n! = n × (n-1) × (n-2) × ... × 2 × 1`
- `0! = 1` (by definition)

---

### 🧪 Example Inputs & Outputs:

- `5! = 5×4×3×2×1 = 120`  
- `3! = 3×2×1 = 6`  
- `0! = 1`  
- `1! = 1`

---

### ✅ Method 1: Iterative Approach

```python
def fact_num(n):
    if n <= 1:
        return 1
    fact = 1
    for num in range(1, n+1):
        fact *= num
    return fact

print(fact_num(5))  # Output: 120
```

---

### ✅ Method 2: Using Recursion

```python
def fact_recursive(n):
    if n <= 1:
        return 1
    return n * fact_recursive(n-1)

print(fact_recursive(5))  # Output: 120
```

---

### ✅ Method 3: Using `math` Module

```python
import math

def facto(n):
    return math.factorial(n)

print(facto(5))  # Output: 120
```

---

### 🧠 Real-World Usage:

- **Permutations & combinations**
- **Probability theory**
- **Mathematical expressions** in calculus and algebra

---

## ✅ 8. Fibonacci Series  

---

### ❓What is the Fibonacci Series?

The Fibonacci Series is a unique sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

---

### 🔢 Mathematical Explanation:

In mathematical terms, the series is defined by the recurrence relation:

```
F(n) = F(n-1) + F(n-2)
```

Where:
- F(0) = 0  
- F(1) = 1

So the series begins as:  
`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`

---

### 📌 Objective:

Given an integer input `n`, find and return the Fibonacci Series up to the Nth term using different methods.

---

### ✅ Method 1: Using Simple Iteration (Loop-based)

```python
def fib_seq(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fib_seq(10)  # Output: 0 1 1 2 3 5 8 13 21 34
```

#### 📘 Explanation:

- Start with `a = 0` and `b = 1`
- Loop `n` times, printing the current value of `a`
- Update `a` and `b` to next Fibonacci pair

---

### ✅ Method 2: Recursive Function

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

for i in range(10):
    print(fib_recursive(i), end=' ')
```

#### 📘 Explanation:

- A direct recursive implementation of the formula
- Very readable, but **inefficient** due to repeated calls

---

### ✅ Method 3: Return Series as a List (Efficient)

```python
def fib_list(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib_list(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### ✅ Method 4: Using Direct Formula (Binet's Formula – Not Always Precise for Large n)

```python
import math

def fib_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-1/phi)**n) / math.sqrt(5))

for i in range(10):
    print(fib_formula(i), end=' ')
```

#### 📘 Note:
May produce floating point inaccuracies for large `n`.

---

### 🧠 Real-World Usage:

- Fibonacci numbers appear in **nature** (petal counts, spiral shells)
- Used in **computer algorithms** (e.g., dynamic programming)
- Also found in **stock market analysis**, **game development**, and **combinatorics**

---

### ✅ Summary Table

| Method            | Description              | Performance       |
|-------------------|--------------------------|-------------------|
| Iterative Loop    | Simple and fast          | ✅ Efficient       |
| Recursion         | Clean but slow           | ❌ Inefficient     |
| Return List       | Stores series as list    | ✅ Good for reuse  |
| Binet’s Formula   | Quick direct math formula| ❌ Slight error    |
```
---

## ✅ 9. Happy Number

---

### ❓What is a Happy Number?

A number is called **happy** if by **repeatedly replacing the number with the sum of squares of its digits**, you eventually get `1`.

If it falls into a cycle and never reaches `1`, it's **not** a happy number.

---

### 🔢 Example:

- 19 →  
  1² + 9² = 82  
  8² + 2² = 68  
  6² + 8² = 100  
  1² + 0² + 0² = 1 ✅

- 4 →  
  4² = 16  
  1² + 6² = 37  
  3² + 7² = 58  
  5² + 8² = 89  
  …loops forever ❌

---

### ✅ Method: Loop with Set to Detect Cycles

```python
def is_happy_number(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        n = total
    return True

print(is_happy_number(19))  # True
print(is_happy_number(4))   # False
```

---

### 🧠 Real-World Use:

- Teaching concepts of **cycle detection**
- Applied in puzzles and mathematical curiosity

---

## ✅ 10. Prime Number Check

---

### ❓What is a Prime Number?

A number that is **greater than 1** and has **no divisors other than 1 and itself**.

---

### 🔢 Examples:

- 2 → ✅ Prime (smallest even prime)  
- 3 → ✅ Prime  
- 4 → ❌ Not Prime  
- 17 → ✅ Prime

---

### ✅ Method 1: Brute Force

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
```

---

### ✅ Method 2: Optimized up to √n

```python
def is_prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

---

### 🧠 Real-World Usage:

- **Cryptography**
- **Random number generators**
- Used in **hashing & compression**

---

## ✅ 11. Prime Numbers in a Range

---

### ❓Objective:
Generate all prime numbers between two values `x` and `y`.

---

### ✅ Method: Use Loop with Prime Check Inside

```python
def prime_range(x, y):
    if x <= 1:
        x = 2
    primes = []

    for i in range(x, y+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

print(prime_range(4, 20))  # Output: [5, 7, 11, 13, 17, 19]
```

---

### 🔍 for-else Note:
The `else` block runs **only if loop is not broken**, hence it's used to detect primes.

---

## ✅ 12. Reverse Digits of a Number

---

### ❓What is Reverse of Digits?

Reverse a number without converting to string.

---

### 🔢 Examples:

- 123 → 321  
- 1001 → 1001  
- 0 → 0

---

### ✅ Method: Digit Manipulation Using While Loop

```python
def rev_digits(n):
    if n <= 0:
        return 'number must be greater than 0'

    rev = 0
    while n > 0:
        dig = n % 10
        rev = dig + rev * 10
        n //= 10
    return rev

print(rev_digits(34567))  # Output: 76543
```

---

## ✅ 13. Square Root of a Number

---

### ❓What is Square Root?

A number `x` is a **square root** of `n` if `x*x == n`.  
We may return the **floor value** if `n` is not a perfect square.

---

### ✅ Method 1: Using Built-in `math.sqrt()`

```python
import math

def sq_root(n):
    return math.sqrt(n)

print(sq_root(49))  # Output: 7.0
```

---

### ✅ Method 2: Using `** 0.5` Operator

```python
def sq_pow(n):
    return n ** 0.5

print(sq_pow(16))  # Output: 4.0
```

---

### ✅ Method 3: Binary Search (Divide and Conquer)

```python
def sqrt_dc(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n

    low = 0
    high = n
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

print(sqrt_dc(35))  # Output: 5
```

---

### 🧠 Real-World Use:

- **Root calculations** in math & physics
- **Game mechanics**, distances, or movement logic

---

### ✅ Summary Table for 7–15

| Concept            | Use/Definition                             | Efficient Way                     |
|--------------------|---------------------------------------------|-----------------------------------|
| Factorial          | Product of integers till `n`                | Use `math.factorial()` or loop   |
| Happy Number       | Sum of squares of digits → ends in 1        | Use set to detect cycles         |
| Prime Number       | Only divisible by 1 and itself              | Check till √n                    |
| Prime in Range     | Find all primes between `x` and `y`         | Use inner loop with break/else   |
| Reverse Digits     | Reverse number (e.g., 123 → 321)            | `%10`, `rev = dig + rev*10`      |
| Square Root        | Return √n (floor if not perfect)            | Use binary search for large `n`  |

---


---

## ✅ 16. Strong Number

---

### ❓What is a Strong Number?

A **strong number** is a number in which the **sum of the factorial of each digit** is equal to the original number.

---

### 🔢 Mathematical Explanation:

If  
```
sum(fact(digit)) == number
```
then it is a Strong Number.

---

### 🧪 Examples:

- 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅  
- 2 → 2! = 2 ✅  
- 123 → 1! + 2! + 3! = 9 ❌

---

### ✅ Python Code:

```python
import math

def is_strong(n):
    temp = n
    result = 0
    while temp > 0:
        digit = temp % 10
        result += math.factorial(digit)
        temp //= 10
    return result == n

print(is_strong(145))  # Output: True
```

---

## ✅ 17. Disarium Number

---

### ❓What is a Disarium Number?

A number is **Disarium** if the **sum of its digits powered with their respective positions** is equal to the number.

---

### 🔢 Mathematical Explanation:

If `n = 135`, then  
1¹ + 3² + 5³ = 1 + 9 + 125 = **135** ✅

---

### ✅ Python Code:

```python
def is_disarium(n):
    digits = list(map(int, str(n)))
    return sum(d ** (i + 1) for i, d in enumerate(digits)) == n

print(is_disarium(135))  # Output: True
```

---

## ✅ 18. Harshad Number (Niven Number)

---

### ❓What is a Harshad Number?

A number is called **Harshad** if it is **divisible by the sum of its digits**.

---

### 🔢 Examples:

- 18 → 1+8 = 9, 18 % 9 == 0 ✅  
- 21 → 2+1 = 3, 21 % 3 == 0 ✅  
- 19 → 1+9 = 10, 19 % 10 ❌

---

### ✅ Python Code:

```python
def is_harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

print(is_harshad(18))  # Output: True
```

---

## ✅ 19. Automorphic Number (Curious Number)

---

### ❓What is an Automorphic Number?

A number is called **automorphic** if its **square ends with the number itself**.

---

### 🔢 Examples:

- 5² = 25 → ends in 5 ✅  
- 76² = 5776 → ends in 76 ✅  
- 7² = 49 → ❌

---

### ✅ Python Code:

```python
def is_automorphic(n):
    return str(n * n).endswith(str(n))

print(is_automorphic(76))  # Output: True
```

---

## ✅ 20. Neon Number

---

### ❓What is a Neon Number?

A **neon number** is a number where the **sum of digits of its square equals the number itself**.

---

### 🔢 Examples:

- 9² = 81 → 8+1 = 9 ✅  
- 1² = 1 → ✅  
- 7² = 49 → 4+9 = 13 ❌

---

### ✅ Python Code:

```python
def is_neon(n):
    return sum(int(d) for d in str(n * n)) == n

print(is_neon(9))  # Output: True
```

---

## ✅ 21. Krishnamurthy Number (Also Strong Number)

**Already covered as Strong Number above.**

---

## ✅ 22. Digital Root

---

### ❓What is a Digital Root?

The **repeated sum of digits** until you get a single-digit number.

---

### 🔢 Examples:

- 456 → 4+5+6 = 15 → 1+5 = **6**  
- 9999 → 9+9+9+9 = 36 → 3+6 = **9**

---

### ✅ Method 1: Loop-based

```python
def digital_root(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

print(digital_root(456))  # Output: 6
```

---

## ✅ 23. Power of Two

---

### ❓What is a Power of 2?

If a number can be expressed as `2^k`, then it is a **power of two**.

---

### 🔢 Examples:

- 8 = 2³ ✅  
- 16 = 2⁴ ✅  
- 10 ❌

---

### ✅ Python Code:

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # Output: True
```

---

## ✅ 24. Armstrong Numbers in a Range

**Already explained under Armstrong, now range form:**

```python
def armstrong_range(x, y):
    result = []
    for n in range(x, y+1):
        digits = len(str(n))
        if n == sum(int(d)**digits for d in str(n)):
            result.append(n)
    return result

print(armstrong_range(100, 999))  # Output: [153, 370, 371, 407]
```

---

## ✅ 25. Magic Number

---

### ❓What is a Magic Number?

A number is called **magic** if **repeated digit sum == 1**.

---

### 🔢 Examples:

- 1729 → 1+7+2+9 = 19 → 1+9 = 10 → 1+0 = 1 ✅  
- 1234 → ❌

---

### ✅ Python Code:

```python
def is_magic(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n == 1

print(is_magic(1729))  # Output: True
```

>>>>>>> 389d692c01511160b53bbc5eb39f55a6c7962362
---