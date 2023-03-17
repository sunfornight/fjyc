import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def pic(i):
    plt.figure(figsize=(10, 7))
    plt.grid()
    plt.scatter(x[i+1], y, s=5)  # 横纵坐标和点的大小
    plt.title(feature_names[i])
    print(feature_names[i], np.corrcoef(x[i+1], y))
    plt.show()
df = pd.read_csv("test6.csv",encoding = 'gbk')
x=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14]]
y=[]
feature_names = ['averagePay','communityName','areaName', 'roomNum', 'levelType', 'acreage', 'houseStructure',
                 'buildingType', 'houseToward', 'buildingStructure', 'decorateSituation', 'floorDoorProportion',
                 'elevator']
y = (df["pay"]).values
x[1] = (df["averagePay"]).values
x[2] = (df["communityName"]).values
x[3] = (df["areaName"]).values
x[4] = (df["roomNum"]).values
x[5] = (df["levelType"]).values
x[6] = (df["acreage"]).values
x[7] = (df["houseStructure"]).values
x[8] = (df["buildingType"]).values
x[9] = (df["houseToward"]).values
x[10] = (df["buildingStructure"]).values
x[11] = (df["decorateSituation"]).values
x[12] = (df["floorDoorProportion"]).values
x[13] = (df["elevator"]).values
for i in range(13):
    pic(i)

