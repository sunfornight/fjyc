from bs4 import BeautifulSoup#引入BeautifulSoup
from urllib import request#引入request
import xlwt

file = xlwt.Workbook()
table = file.add_sheet('test1')
n=0
Id = []
pay = []
averagePay = []
communityName = []
areaName = []
roomNum = []
# sittingRoom = []
# kitchenNum = []
# lavatoryNum = []
levelType = []
# levelNum = []
acreage = []
houseStructure = []
internalArea = []
buildingType = []
houseToward = []
buildingStructure = []
decorateSituation = []
floorDoorProportion = []
elevator = []

table.write(0,0,label='ID')
table.write(0,1,label='平均房价')
table.write(0,2,label='小区名称')
table.write(0,3,label='所在区域')
table.write(0,4,label='房屋户型')
table.write(0,5,label='所处楼层')
table.write(0,6,label='建筑面积')
table.write(0,7,label='户型结构')
table.write(0,8,label='套内面积')
table.write(0,9,label='建筑类型')
table.write(0,10,label='房屋朝向')
table.write(0,11,label='建筑结构')
table.write(0,12,label='装修情况')
table.write(0,13,label='梯户比例')
table.write(0,14,label='配备电梯')
table.write(0,15,label='房价')


def pages(url):
   # url = 'https://nc.lianjia.com/ershoufang/xinjianqu/'
    global n
    head = {}
    req = request.Request(url,headers=head)
    response = request.urlopen(req)
    html_data = response.read()
    soup = BeautifulSoup(html_data,'html.parser')
    soup_texts = soup.find('ul',class_='sellListContent')
    for son in soup_texts:
        if son !='\n':
            n=n+1
            print('房源信息',n)
            Id.append(n)
            print(Id)
            table.write(n, 0, label=n)
            href=son.a.get('href')
            #print(href)
            head2 = {}
            req2 = request.Request(href, headers=head2)
            response2 = request.urlopen(req2)
            html_data2 = response2.read()
            soup2 = BeautifulSoup(html_data2, 'html.parser')
            soup2_texts = soup2.find('div',class_='introContent')
            #soup3_texts = soup2.find('div', class_='transaction')
            soup4_texts = soup2.find('span', class_='total')
            soup5_texts = soup2.find('span', class_='unitPriceValue')
            soup6_texts = soup2.find('div', class_='communityName').a
            soup7_texts = soup2.find('div', class_='areaName')
            pay_=soup4_texts.text
            pay.append(pay_)
            print(pay)
            table.write(n, 15, label=pay_)

            community_name=soup6_texts.text
            communityName.append(community_name)
            print(communityName)
            table.write(n, 2, label= community_name)

            average_pay=(soup5_texts.text.replace("元/平米",""))
            averagePay.append(average_pay)
            print(averagePay)
            table.write(n, 1, label=average_pay)

            area_name=soup7_texts.text.replace("所在区域","").replace("新建区","").strip()
            area_name.split()
            areaName.append(area_name)
            print(areaName)
            table.write(n, 3, label=area_name)

            tag = 0
            # print(tag)
            for son2 in soup2_texts.ul.children:
                if son2 != '\n':
                    tag+=1
                    txt=son2.get_text()
                    L=list(txt)
                    L.insert(4,'|')
                    txt="".join(L)
                    text=txt.split('|')[1].strip()
                    text=text.split(" ")
                    str=text[0]
                    #print(text)
                    if tag==1:
                        roomNum.append(str)
                        print(roomNum)
                        table.write(n, 4, label=str)
                    # elif tag==2:
                    #     sittingRoom.append(str)
                    #     print(sittingRoom)
                    # elif tag==3:
                    #     kitchenNum.append(str)
                    #     print(kitchenNum)
                    # elif tag==4:
                    #     lavatoryNum.append(str)
                    #     print(lavatoryNum)
                    elif tag==2:
                        levelType.append(text[0])
                        print(levelType)
                        table.write(n, 5, label=str)
                        #levelNum.append(text[0])
                        #print(levelNum)
                    elif tag == 3:
                        acreage.append(str)
                        print(acreage)
                        table.write(n, 6, label=str)
                    elif tag == 4:
                        houseStructure.append(str)
                        print(houseStructure)
                        table.write(n, 7, label=str)
                    elif tag == 5:
                        internalArea.append(str)
                        print(internalArea)
                        table.write(n, 8, label=str)
                    elif tag == 6:
                        buildingType.append(str)
                        print(buildingType)
                        table.write(n, 9, label=str)
                    elif tag == 7:
                        houseToward.append(str)
                        print(houseToward)
                        table.write(n, 10, label=str)
                    elif tag == 8:
                        buildingStructure.append(str)
                        print(buildingStructure)
                        table.write(n, 11, label=str)
                    elif tag == 9:
                        decorateSituation.append(str)
                        print(decorateSituation)
                        table.write(n, 12, label=str)
                        # if str=="精装":
                        #     table.write(n, 12, label=1)
                        #     elevator.append(1)
                        # else:
                        #     table.write(n, 12, label=0)
                        #     elevator.append(0)
                    elif tag == 10:
                        floorDoorProportion.append(str)
                        print(floorDoorProportion)
                        table.write(n, 13, label=str)
                    elif tag == 11:
                        elevator.append(str)
                        table.write(n,14,label=str)
                        print(elevator)
                        # if str=="有":
                        #     table.write(n, 14, label=1)
                        #     elevator.append(1)
                        # else:
                        #     table.write(n, 14, label=0)
                        #     elevator.append(0)



            # for son3 in soup3_texts.ul:
            #     txt = son3.get_text()
            #     L = list(txt)
            #     L.insert(4, '|')
            #     txt = "".join(L)
            #     print(txt.split('|')[1])

def run():
    for i in range(1,101):
        url=("https://nc.lianjia.com/ershoufang/xinjianqu/pg{}/".format(i))
        pages(url)
        print("第{}页".format(i))

run()
#file.save("test4.xls")




