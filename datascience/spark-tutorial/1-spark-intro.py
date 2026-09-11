"""Distributed Pandas in PySpark"""
""" Method 1
Yes, you can work with distributed pandas DataFrames using PySpark's Pandas API on Spark (formerly known as Koalas, 
which was integrated directly into PySpark starting with Spark 3.2). This allows you to execute standard pandas syntax distributed across a Spark cluster without rewriting your codebase."""


import pyspark.pandas as ps

# Creates a distributed pandas DataFrame backed by Spark
ps_df = ps.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})



"""Method 2

Converting a Pandas DataFrame to a Spark DataFrame

To convert a standard local pandas DataFrame into a distributed native Spark DataFrame, 
use the spark.createDataFrame() method."""

import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("PandasToSpark").getOrCreate()

# Create a standard pandas DataFrame
pandas_df = pd.DataFrame(
    {"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]}
)

# Convert to a Spark DataFrame  
spark_df = spark.createDataFrame(pandas_df)

# Show the distributed dataset
spark_df.show()


"""Recommended to use pyspark native file read functions to create pyspark dataframes"""
