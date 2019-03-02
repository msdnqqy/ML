#使用sklearn实现K近邻算法

import numpy as np;
from sklearn import datasets;
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#导入花数据集
iris=datasets.load_iris()
iris_x=iris.data
iris_y=iris.target
print(iris_x[:2,:])

#切分验证集和训练集并打乱顺序
x_train,x_test,y_train,y_test=train_test_split(iris_x,iris_y,test_size=0.3)

print(y_train)

#定义使用模型
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)

prediction=knn.predict(x_test)

#输出预测结果
print(prediction)
print(y_test)
