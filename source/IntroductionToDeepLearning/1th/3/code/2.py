import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

def step_func(x):
    y = x > 0
    return np.array(x > 0, dtype=int)

def step_func1(x):
    y = x > 0
    return y.astype(int)


print(f"step_func(0) {step_func(0)}")
print(f"step_func(1) {step_func(1)}")
tmp1 = np.array([1.0, 2.0, 3.0])
print(f"step_func(tmp1) {step_func(tmp1)}")


x = np.arange(-5.0, 5.0, 0.1)
y = step_func(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
