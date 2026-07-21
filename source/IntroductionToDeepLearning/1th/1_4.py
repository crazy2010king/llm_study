import numpy as np

X = np.array([[51,55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])


for row in X:
    print(row)

#print(f"X3"{X[np.array([0, 2, 4])]})
print(f"X1 {X}")    
X = X.flatten()
print(f"X2 {X}")


print(f"X3 {X}")
X[np.array([0, 2, 4])]
print(f"1 {X[np.array([0, 2, 4])]}")
print(f"2 {X > 15}")
print(f"3 {X[X>15]}]")





