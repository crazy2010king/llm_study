import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
tmp1 = x*w
tmp2 = np.sum(x*w)
tmp3 = np.sum(x*w)+b
print(f"tmp1 {tmp1} tmp2 {tmp2} tmp3 {tmp3}")
