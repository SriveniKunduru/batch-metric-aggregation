# Databricks notebook source
from pyspark.sql.functions import col, to_date, avg, min, max

# Sample input data
raw_data = [
    ("temperature", 88.0, "2022-06-04T12:01:00.000Z"),
    ("temperature", 89.0, "2022-06-04T12:01:30.000Z"),
    ("precipitation", 0.5, "2022-06-04T14:23:32.000Z")
]

columns = ["metric", "value", "timestamp"]

# Creating a DataFrame
df = spark.createDataFrame(raw_data, schema=columns)

# Extracting the date portion of the timestamp to define daily time buckets
df_with_date = df.withColumn("date", to_date(col("timestamp")))

# Performing the aggregation: average, minimum, and maximum per metric per day
aggregated = df_with_date.groupBy("date", "metric").agg(
    avg("value").alias("avg_value"),
    min("value").alias("min_value"),
    max("value").alias("max_value")
)

# Displaying the final result
display(aggregated)
