from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r'C:\Users\AY\Desktop\PythonCode 3.10.11\venv\Scripts\python.exe'

# create SparkConf Object - setMaster normal on distribution server, but in our case we use local("local[*]")
conf = SparkConf().setMaster('local[*]').setAppName('MyFirstPySparkApp')

# on the basis of sparkConf create SparkContext object
sc = SparkContext(conf=conf)

# create RDD
rdd = sc.parallelize([1,2,3,4,5])
rdd_2 = sc.parallelize(['Python3.10.11','Python Spark','i am learning Python Spark'])
rdd_3 = sc.parallelize([('Man',99),('Man',88),('Woman',99),('Woman',66),('Woman',1)])

# Option 1 with function
# def func(data):
#     return data * 10
# use map method
# rdd2 = rdd.map(func)
# Option 2 with Lambda - with chain invoke
# new_rdd = rdd.map(lambda x:x*10).map(lambda x:x+5)

# flatMap
# new_rdd_2 = rdd_2.map(lambda x:x.split(' '))
# new_rdd_2_1 = rdd_2.flatMap(lambda x:x.split(' '))
# print(new_rdd_2.collect())
# print(new_rdd_2_1.collect())

# reduceByKey
new_rdd_3 = rdd_3.reduceByKey(lambda a,b:a+b)
print(new_rdd_3.collect())



# show the version of PySpark
print('The version of PySpark is: '+sc.version)

# stop SparkContext object (stop PySpark)
sc.stop()