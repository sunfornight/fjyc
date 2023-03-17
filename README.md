# fjyc
基础——房价预测
链家网——南昌市新建区二手房!
![image](https://user-images.githubusercontent.com/36923547/225801676-67e804ce-db13-473e-87dd-b2842bc03d1c.png)
![image](https://user-images.githubusercontent.com/36923547/225801726-55574804-c1da-48fd-9c4c-7331e9274b04.png)
爬取结果（3000条信息，目前15条属性）：
![image](https://user-images.githubusercontent.com/36923547/225801770-e81c3242-26e0-4e0e-944a-6d1d5b5bd5e7.png)
借用pandas将所有字符串转成数字向量：
![image](https://user-images.githubusercontent.com/36923547/225801826-4cdd6338-c9e2-48c7-8971-1d51d8c710ec.png)
分别以每个属性作为横坐标，房价作为纵坐标画出散点图以及它们的相关系数
![image](https://user-images.githubusercontent.com/36923547/225801870-19dbc85a-0298-487d-9c66-30c68d41c28c.png)
![image](https://user-images.githubusercontent.com/36923547/225801878-cddbcd3f-be8c-45cc-b30c-19dc8f109bf2.png)
将数据放到paddle模型中跑
![image](https://user-images.githubusercontent.com/36923547/225801950-1ce14ea0-e6ab-4c83-86af-44edf39119c8.png)
该模型预测10次结果:
![1679022264259](https://user-images.githubusercontent.com/36923547/225802008-92f22216-8bd2-401f-87a9-1508ecf86799.png)
