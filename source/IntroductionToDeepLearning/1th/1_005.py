import numpy as np
import scipy.special
#手动实现 Softmax（防上溢/下溢）：manual_softmax(x)

def manual_softmax(x):
    if x.ndim != 2:
        raise ValueError("假定输入为 (Batch_Size, Classes) 的二维特征图")

    row_max = x.max(axis=1, keepdims=True)
    print(f"row_max {row_max} x {x} ")
    x_shifted = x - row_max
    
    exp_x = np.exp(x_shifted)
    
    print(f"x_shifted {x_shifted} exp_x {exp_x} ")
    
    sum_exp = exp_x.sum(axis=1, keepdims=True)
    print(f"sum_exp {sum_exp} exp_x {exp_x} ")
    return exp_x / sum_exp

logits = np.array([[1000.0, 1001.0, 999.0], [-10.0, 0.0, 10.0]])
res_manual = manual_softmax(logits)
res_scipy = scipy.special.softmax(logits, axis=1)
print(f"res_manual {res_manual} res_scipy {res_scipy} ")
assert np.allclose(res_manual, res_scipy), "Softmax 逻辑不一致或发生了溢出！"
print("✅ 模块 3：防溢出 Softmax 验证通过！")