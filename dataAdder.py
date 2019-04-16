# url = 'http://192.168.178.10/?JSON'
import json
import urllib.request
with urllib.request.urlopen("http://192.168.178.10/?JSON") as url:
    data = json.loads(url.read().decode())
    print(data)
# weatherList = json.loads(response.read())
# print(weatherList)
# jsonDataList = [[],[]]
# master = Tk()
# screeny = 25
# #creating text screen for non-int data
# text = Text(master)
# Sbar = Scrollbar(master)
# Sbar.pack(side=RIGHT, fill=Y)
# text.pack(side=LEFT, fill=Y)
# for data in weatherList:
#         for x in range(0,1):
#             if data['title'] not in jsonDataList[x]:
#                 jsonDataList[x].append(data['title'])
# def getData():
#     for data in weatherList:
#         for x in range(0,1):
#             if data['value'] not in jsonDataList[x]:
#                 jsonDataList[x+1].append(data['value'])
#     print(jsonDataList)
#     #print(str(jsonDataList[1][1]))