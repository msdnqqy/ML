#sklearn 构造数据

#导入数据，导入训练模型
from sklearn import datasets;
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=1)
plt.scatter(x,y)
plt.show()