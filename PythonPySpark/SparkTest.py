print('that is my first PySpark Code')

# That is the PySpark Formal forever and ever
# Never change til PySpark changes it
from pyspark import SparkConf,SparkContext
import os
#define the PySpark Environment
os.environ['PYSPARK_PYTHON'] = r'C:\Users\AY\Desktop\pythonCode\python\Scripts\python.exe'
# create SparkConf Object - setMaster normal on distribution server, but in our case we use local("local[*]")
conf = SparkConf().setMaster('local[*]').setAppName('MyFirstPySparkApp')
# on the basis of sparkConf create SparkContext object
sc = SparkContext(conf=conf)

# show the version of PySpark
print('The version of PySpark is: '+sc.version)

# stop SparkContext object (stop PySpark)
sc.stop()