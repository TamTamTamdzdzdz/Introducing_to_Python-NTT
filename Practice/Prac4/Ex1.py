import numpy as np

a = np.arange(1, 21).reshape(4, 5).T.reshape(4, 5)
# Tạo ma trận 1*20 xong r chuyển thành 4*5. Sau đó chuyển vị thành 5*4 và lại chuyển lại thành ma trận 4*5
print(a)
