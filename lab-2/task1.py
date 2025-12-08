import random
import math

nums = [random.randint(0, 100) for _ in range(20)]
result1 = [num for num in nums if num <= 50]
print(f"Початкові: {nums}")
print(f"Результат: {result1}")
