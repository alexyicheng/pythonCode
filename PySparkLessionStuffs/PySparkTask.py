# 18.11.2024

from pyspark import SparkConf,SparkContext
import os

# set up PySpark Environment
os.environ['PYSPARK_PYTHON'] = r'C:\Users\AY\Desktop\PythonCode 3.10.11\venv\Scripts\python.exe'
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf = conf)

# read txt
rdd = sc.textFile(r'C:\Users\AY\Desktop\PythonCode 3.10.11\PySparkLessionStuffs\hello.txt')

# get the data from txt
word_rdd = rdd.flatMap(lambda x:x.split(' '))
# print(word_rdd.collect())

# single word of list into tuple
word_with_one_rdd = word_rdd.map(lambda word:(word,1))
# print(word_with_one_rdd.collect())

# sum the tuple
result_rdd = word_with_one_rdd.reduceByKey(lambda a,b:a+b)

print(result_rdd.collect())
