import numpy as np

# 手动实现矩阵乘法：manual_matmul(x, y)
def manual_matmul(x, y):    
    if x.ndim != 2 or y.ndim != 2:
        raise ValueError("仅支持二维矩阵乘法进行硬核体验")
    if x.shape[1] != y.shape[0]:
        raise ValueError(f"矩阵内侧维度不匹配: {x.shape[1]} vs {y.shape[0]}")
    H, W_mid = x.shape
    _, W_out = y.shape
    print(f"H {H} W_mid {W_mid}")
    print(f"_ {_} W_out {W_out}")
    
    # 预先开辟一整块连续内存空间
    out = np.zeros((H, W_out), dtype = np.float64)
    
    for i in range(H):
        for j in range(W_out):
            sum_val = 0.0
            for k in range(W_mid):
                sum_val += x[i, k] * y[k, j]
                print(f"i {i} k {k} x[i, k] {x[i, k]}, j{j} y[k, j] {y[k, j]}")                
            out[i, j] = sum_val
            print(f"i {i} j {j} out[i, j] {out[i, j]}")                
    return out

x_mat = np.random.randn(5, 8)
y_mat = np.random.randn(8, 4)
assert np.allclose(manual_matmul(x_mat, y_mat), x_mat @ y_mat)
print("✅ 模块 2：三层循环矩阵乘法验证通过！")
