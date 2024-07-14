import pandas as pd
from pyspark.sql import SparkSession
import plotly.express as px

# Créer une session Spark
spark = SparkSession.builder \
    .appName("PySpark HDFS Example") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

# Lire le fichier CSV depuis HDFS
df = spark.read.csv("hdfs://localhost:9000/user/hadoop/imdb-movies-dataset.csv", header=True, inferSchema=True)

# Assurer la conversion de la colonne Year en entier
df = df.withColumn("Year", df["Year"].cast("int"))

# Compter les films par année
movies_per_year = df.groupBy("Year").count().orderBy("Year")

# Convertir le DataFrame Spark en Pandas DataFrame pour utilisation avec Plotly
pandas_df = movies_per_year.toPandas()

# Tracer les résultats avec Plotly
fig = px.line(pandas_df, x='Year', y='count', title='Number of Movies per Year', markers=True)

# Afficher le graphique dans le navigateur
fig.show()

# Enregistrer le graphique en tant que fichier HTML pour vérification
fig.write_html("movies_per_year.html")

# Afficher un message indiquant que le fichier a été créé
print("Le graphique a été enregistré dans le fichier movies_per_year.html")

# Arrêter la session Spark
spark.stop()
