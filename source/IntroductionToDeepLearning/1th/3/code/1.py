import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

def step_func(x):
    if x <= 0:
        return 0
    else:
        return 1
    
def step_func1(x):
    y = x > 0
    return y.astype(int)
    
    
print(f"step_func(0) {step_func(0)}")
print(f"step_func(1) {step_func(1)}")

tmp1 = np.array([1.0, 2.0, 3.0])
print(f"step_func1(tmp1) {step_func1(tmp1)}")
tmp2 = np.array([-1.0, -2.0, 3.0])
print(f"step_func1(tmp2) {step_func1(tmp2)}")
