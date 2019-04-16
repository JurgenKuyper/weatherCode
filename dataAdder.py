import json
import urllib.request
response = urllib.request.urlopen("http://192.168.178.10/?JSON")
print(response)
weatherList = json.load(response.text)
print(weatherList)
# jsonDataList = [[],[]]
# for data in weatherList:
#         for x in range(0,1):
#             if data['title'] not in jsonDataList[x]:
#                 jsonDataList[x].append(data['title'])
# def getData():
#     #print(time1[5])
#     for data in weatherList:
#         for x in range(0,1):
#             if data['value'] not in jsonDataList[x]:
#                 jsonDataList[x+1].append(data['value'])
#     print(jsonDataList)
#     #print(str(jsonDataList[1][1]))