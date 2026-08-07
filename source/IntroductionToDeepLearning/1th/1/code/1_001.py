import numpy as np

x = np.random.randn(32, 784)
print(f"x {x}")


w = np.random.randn(784, 128)
print(f"w {w}")


b = np.random.randn(128)
print(f"b {b}")

y = x @ w +b 

print(f"y {y}")