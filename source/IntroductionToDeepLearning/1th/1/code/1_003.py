import numpy as np

# 手动模拟广播：manual_broadcast(a, b)
def manual_broadcast(a, b):
    # 1. 自动向左补齐维度 (例如: a=(3,), b=(4,3) -> a_shape=(1,3))
    a_shape = list(a.shape)
    b_shape = list(b.shape)
    print(f"a {a}")
    print(f"a_shape {a_shape}")
    print(f"b {b}")
    print(f"b_shape {b_shape}")
    
    while len(a_shape) < len(b_shape):
        a_shape.insert(0, 1)
    while len(b_shape) < len(a_shape):
        b_shape.insert(0, 1)
        
    print(f"a1 {a}")
    print(f"a1_shape {a_shape}")
    print(f"b1 {b}")
    print(f"b1_shape {b_shape}")
    
    a_reshaped = a.reshape(a_shape)
    print(f"a {a}")
    print(f"a_reshaped {a_reshaped}")
    b_reshaped = b.reshape(b_shape)
    print(f"b {b}")
    print(f"b_reshaped {b_reshaped}")
    
    # 2. 计算目标广播形状
    target_shape = []
    for dim_a, dim_b in zip(a_shape, b_shape):
        if dim_a == dim_b:
            target_shape.append(dim_a)
        elif dim_a == 1:
            target_shape.append(dim_b)
        elif dim_b == 1:
            target_shape.append(dim_a)
        else:
            raise ValueError(f"Operands could not be broadcast together with shapes {a.shape} {b.shape}")
        print(f"target_shape {target_shape} dim_a {dim_a} dim_b {dim_b}")
        
    a_broadcasted = a_reshaped.copy()
    b_broadcasted = b_reshaped.copy()
    print(f"0--a_broadcasted {a_broadcasted}")
    print(f"0--b_broadcasted {b_broadcasted}")
    
    for axis, (dim_a, dim_b) in enumerate(zip(a_shape, b_shape)):
        if dim_a == 1 and dim_b > 1:
            a_broadcasted = np.repeat(a_broadcasted, dim_b, axis=axis)
        if dim_b == 1 and dim_a > 1:
            b_broadcasted = np.repeat(b_broadcasted, dim_a, axis=axis)   
        print(f"a_broadcasted {a_broadcasted} dim_a {dim_a} dim_b {dim_b} axis {axis}")
        print(f"b_broadcasted {b_broadcasted} dim_a {dim_a} dim_b {dim_b} axis {axis}") 
    
    return a_broadcasted, b_broadcasted

a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
bc_a, bc_b = manual_broadcast(a, b)
res_manual = bc_a + bc_b
res_native = a + b
assert np.array_equal(res_manual, res_native)
print("手动广播验证通过！")
