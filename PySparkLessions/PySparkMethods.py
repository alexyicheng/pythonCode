# 17.11.2024

# current now python 3.12.6 desonot support pyspark
# https://community.cloudera.com/t5/Community-Articles/Spark-Python-Supportability-Matrix/ta-p/379144

from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = 'C:/Users/AY/Desktop/pythonCode/python/Scripts/python.exe'

# create SparkConf Object - setMaster normal on distribution server, but in our case we use local("local[*]")
conf = SparkConf().setMaster('local[*]').setAppName('MyFirstPySparkApp')

# on the basis of sparkConf create SparkContext object
sc = SparkContext(conf=conf)

# create RDD
rdd = sc.parallelize([1,2])

def func(data):
    return data * 10

# use map method
rdd2 = rdd.map(func)
print(rdd2.collect())

# show the version of PySpark
print('The version of PySpark is: '+sc.version)

# stop SparkContext object (stop PySpark)
sc.stop()