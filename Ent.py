import numpy as np
import pandas as pd

"""
计算信息熵
1.获取各类的数量
2.计算各类概率
3.Ent=sum（px*log2px）
"""
def calEnt(dataSet,index):
    data=pd.DataFrame(dataSet)
    count=data.iloc[:,index].value_counts()
    px=np.array(count/data.shape[0])
    Ent=(-px*np.log2(px)).sum()
    return Ent


"""
计算信息增益
1.信息增益=Ent（D）-sum（pDv*Ent（Dv））
2.获取该列的所有属性值
3.带入公式
"""
def calEntPurity(dataSet,index,targetIndex):
    data=pd.DataFrame(dataSet)
    dataObj={}

    #获取分类
    keys=data.iloc[:,index].value_counts().index

    #划分数据集，分别计算信息熵
    EntsDv=[]
    for key in keys:
        dataSplit=data[data.iloc[:,index]==key].copy()
        #计算当前类别的信息熵
        EntD=calEnt(dataSplit,targetIndex)
        #乘以权重
        EntD*=(dataSplit.shape[0]/data.shape[0])
        EntsDv.append(EntD)

    EntPurity=calEnt(data,targetIndex)-np.array(EntsDv).sum()
    return EntPurity

"""
切分数据集
"""
def splitData(dataSplit,index):
    #根据index获取列明
    colname=dataSplit.columns[index]

    dataSplitComplete=dataSplit.copy().drop(colname,axis=1)
    return dataSplitComplete

"""
建立决策树
递归构建决策树

1.
"""
def buildTree(dataSet,targetIndex):
    pass


if __name__=="__main__":
    dataobj={"no surfacing":[1,1,1,0,0],"flippers":[1,1,0,1,1],"fish":["yes","yes","no","no","no"]}
    print("信息熵：",calEnt(dataobj,-1))

    es=calEntPurity(dataobj,0,-1)
    print("信息增益：",es)

    #数据集构建
    index=['色泽',    '根蒂',    '敲声',    '纹理',    '脐部',    '触感',    '好瓜']


 [['青绿',    '蜷缩',    '浊响',    '清晰',    '凹陷',    '硬滑','是'],
 [ '乌黑',    '蜷缩',    '沉闷',    '清晰'    ,'凹陷'    ,'硬滑',    '是'],
  ['乌黑',    '蜷缩'    ,'浊响'    ,'清晰'    ,'凹陷'    ,'硬滑'    ,'是']
  ['青绿',    '蜷缩',    '沉闷',    '清晰',    '凹陷',    '硬滑',    '是'],
  ['浅白',    '蜷缩',    '浊响',    '清晰','凹陷'    ,'硬滑'    ,'是']
  ['青绿',    '稍蜷',    '浊响'    ,'清晰'    ,'稍凹',    '软粘'    ,'是']
 乌黑    稍蜷    浊响    稍糊    稍凹    软粘    是
 乌黑    稍蜷    浊响    清晰    稍凹    硬滑    是
 乌黑    稍蜷    沉闷    稍糊    稍凹    硬滑    否
 青绿    硬挺    清脆    清晰    平坦    软粘    否
 浅白    硬挺    清脆    模糊    平坦    硬滑    否
 浅白    蜷缩    浊响    模糊    平坦    软粘    否
 青绿    稍蜷    浊响    稍糊    凹陷    硬滑    否
 浅白    稍蜷    沉闷    稍糊    凹陷    硬滑    否
 乌黑    稍蜷    浊响    清晰    稍凹    软粘    否
 浅白    蜷缩    浊响    模糊    平坦    硬滑    否
 青绿    蜷缩    沉闷    稍糊    稍凹    硬滑    否