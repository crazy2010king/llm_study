import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(f"AND(0, 0) {AND(0, 0)}")
print(f"AND(1, 0) {AND(1, 0)}")
print(f"AND(2, 2) {AND(2, 2)}")
print(f"AND(1, 1) {AND(1, 1)}")\
    


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(f"NAND(0, 0) {NAND(0, 0)}")
print(f"NAND(1, 0) {NAND(1, 0)}")
print(f"NAND(2, 2) {NAND(2, 2)}")
print(f"NAND(1, 1) {NAND(1, 1)}")



def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(f"OR(0, 0) {OR(0, 0)}")
print(f"OR(1, 0) {OR(1, 0)}")
print(f"OR(2, 2) {OR(2, 2)}")
print(f"OR(1, 1) {OR(1, 1)}")


def NOR(x1, x2):
    S1 = NAND(x1, x2)
    S2 = OR(x1, x2)
    Y = NAND(S1, S2)
    return Y

print(f"NOR(0, 0) {NOR(0, 0)}")
print(f"NOR(1, 0) {NOR(1, 0)}")
print(f"NOR(2, 2) {NOR(2, 2)}")
print(f"NOR(1, 1) {NOR(1, 1)}")