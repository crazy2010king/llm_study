import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np


x = np.array([[1.0, 2.0], [1.2, 2.2]])
print(f"np.ndim(x) {np.ndim(x)}, np.shape(x) {np.shape(x)}")

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 3], [4, 5]])

print(f"np.dot(a, b) {np.dot(a, b)}")
print(f"np.dot(b, a) {np.dot(b, a)}")
