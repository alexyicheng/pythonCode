# 17.11.2024
from pyspark.errors import PySparkException

# how does PySpark work
# 1.import Data
# 2.calculate Data
# 3.export Data

# RDD (Resilient Distribution Datasets)
# data saved as RDD Object in Py
# calculate methode and return always with RDD object and methode



from pyspark import SparkConf,SparkContext

# create SparkConf Object - setMaster normal on distribution server, but in our case we use local("local[*]")
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# on the basis of sparkConf create SparkContext object
sc = SparkContext(conf=conf)

# transform list,tuple,set,dict or str into RDD Object
# rdd = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((2,3,5,4,6))
# rdd3 = sc.parallelize('abcdefg')
# rdd4 = sc.parallelize({10,12,15,16,17})
# rdd5 = sc.parallelize({'key':'value','key1':'value1'})

# if you want to know, which element into RDD, you have to use collect()
# print(rdd.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# over textfile methode to read data into Spark as RDD Object
rdd_txt = sc.textFile('joke.txt')
print(rdd_txt.collect())

# show the version of PySpark
print('The version of PySpark is: '+sc.version)

# stop SparkContext object (stop PySpark)
sc.stop()