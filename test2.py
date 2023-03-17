import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth',1000)

data=pd.read_csv("test4.csv",encoding = 'gbk')
data["communityName"]=pd.factorize(data["communityName"])[0].astype(np.uint16)
data["areaName"]=pd.factorize(data["areaName"])[0].astype(np.uint16)
data["roomNum"]=pd.factorize(data["roomNum"])[0].astype(np.uint16)
data["levelType"]=pd.factorize(data["levelType"])[0].astype(np.uint16)
data["houseStructure"]=pd.factorize(data["houseStructure"])[0].astype(np.uint16)
data["houseToward"]=pd.factorize(data["houseToward"])[0].astype(np.uint16)
data["buildingStructure"]=pd.factorize(data["buildingStructure"])[0].astype(np.uint16)
data["buildingType"]=pd.factorize(data["buildingType"])[0].astype(np.uint16)
data["decorateSituation"]=pd.factorize(data["decorateSituation"])[0].astype(np.uint16)
data["floorDoorProportion"]=pd.factorize(data["floorDoorProportion"])[0].astype(np.uint16)
data["elevator"]=pd.factorize(data["elevator"])[0].astype(np.uint16)
a=pd.DataFrame(data)
print(a)
a.to_csv("test6.csv")

