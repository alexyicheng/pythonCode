# 17.11.2024

from pyspark import SparkConf,SparkContext
# create SparkConf Object - setMaster normal on distribution server, but in our case we use local("local[*]")
conf = SparkConf().setMaster('local[*]').setAppName('MyFirstPySparkApp')
# on the basis of sparkConf create SparkContext object
sc = SparkContext(conf=conf)

# show the version of PySpark
print('The version of PySpark is: '+sc.version)

# stop SparkContext object (stop PySpark)
sc.stop()


