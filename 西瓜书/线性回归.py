#sklearn 实现线性回归

#导入数据，导入训练模型
from sklearn import datasets;
from sklearn.linear_model import LinearRegression

#导入数据集
data=datasets.load_boston()
data_x,data_y=data.data,data.target

#定义模型
model=LinearRegression()

#训练模型
model.fit(data_x,data_y)

#使用模型预测
prediction=model.predict(data_x[:4])
print(prediction)
print(data_y[:4])