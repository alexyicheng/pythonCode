import sys

import requests
from bs4 import BeautifulSoup


string = 'Interview'
new_string = string.replace('e','-',1)
# print(new_string)

# url = 'https://www.stepstone.de//jobs--Data-Analyst-Talanx-Group-Reinsurance-Hannover-HDI-AG--11601397-inline.html'
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#     'referer':'https://www.stepstone.de/work/analyst-data'
# }
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,'lxml')
# print(soup)

# links = [0,2,35,454,515]
# count = 0
# for newlink in links:
#     print(newlink)
#     print(count)
#     count += 1


# class Kind(object):
#     def __init__(self):
#         self.name = 'Ludan'
#     def eat(self):
#         print(f'{self.name} is eating')
#
# k = Kind()
# print(k.eat())

# dic_color = {'red':'rot','green':'Grün','gold':'金色','brown':'braun','purple':'violett'}
# print(dic_color['gold'])
#
# hero = [
#     'Ahri','Akail','Ashe','Master Yi','Soraka','Teemo','Morgana','Olaf'
# ]
# print(len(hero))

# import sys
# print(sys.executable)
# print(sys.path)

# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder \
#     .appName("Test PySpark") \
#     .getOrCreate()
#
# data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
# df = spark.createDataFrame(data, ["ID", "Name"])
# df.show()
#
# spark.stop()


l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [1,2,3,4,5,6,7,8,9]
print(len(l2))
for elements in range(len(l2)):
   l2[elements]  *= 10
   # l2[elements] = elements * 10 # difference start with l2[0] = 0 and end with l2[9] = 8
print(l2)

# l2 = [elements * 10 for elements in l2]
# print(l2)


student_info= [{'id':1,'name':'Alex'},{'id':2,'name':'Olga'}]
del_id = 1
del student_info[del_id]
print(student_info)
