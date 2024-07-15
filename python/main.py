from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import plotly.express as px

# Spark Session
spark = SparkSession.builder \
    .appName("PySpark HDFS Example") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

df = spark.read.csv("hdfs://localhost:9000/user/hadoop/imdb-movies-dataset.csv", header=True, inferSchema=True)


spark.stop()
