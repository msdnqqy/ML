from sklearn import tree;
from sklearn.datasets import load_wine;
from sklearn.model_selection import train_test_split
import pandas as pd;
import graphviz


#导入红酒数据集
wine=load_wine()
wine_df=pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
wine_df.head()

#拆分数据集
x_train,x_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3)
x_train.shape


#声明决策树模型
model=tree.DecisionTreeClassifier(
    criterion="entropy"
    ,random_state=30
    ,splitter="random"
    ,max_depth=5
    ,min_samples_leaf=10
    ,min_samples_split=10
)


#训练模型
model.fit(x_train,y_train)
print("score:",model.score(x_test,y_test))

#验证决策树的分类结果，这里就不构造新数据了，直接用红酒数据的第一个条
wine.data[0]
print(model.predict_proba([wine.data[0]]))
print(model.predict([wine.data[0]]))

#输出决策树
dot_data=tree.export_graphviz(
    model
    ,feature_names=wine.feature_names
    ,class_names=['琴酒','雪莉','贝尔摩德']
    ,filled=True
    ,rounded=True
    ,out_file=None)
graph=graphviz.Source(dot_data)
graph
