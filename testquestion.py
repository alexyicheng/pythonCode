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

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test PySpark") \
    .getOrCreate()

data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
df = spark.createDataFrame(data, ["ID", "Name"])
df.show()

spark.stop()
