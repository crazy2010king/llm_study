import matplotlib.pyplot as plt
from matplotlib.image import imread

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1+ x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
    print(a)
    
    
print(f"AND(0, 0) {AND(0, 0)}")
print(f"AND(1, 0) {AND(1, 0)}")
print(f"AND(2, 2) {AND(2, 2)}")
print(f"AND(1, 1) {AND(1, 1)}")
