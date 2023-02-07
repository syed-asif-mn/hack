import subprocess
import os
import csv
import sys
import time
import json
import numpy as np
from kafka import KafkaProducer
from Initializer import Initialize
from datetime import datetime,timedelta
from pyspark.sql import DataFrame, SparkSession, functions

spark = SparkSession.builder.appName("House Price Prediction").getOrCreate()
init_object = Initialize()

KAFKA_BROKER = os.getenv("KAFKA_BROKER")

class kafka_producer():
    def publish_message(self,producer_instance, topic_name, key, value):
        try:
            key_bytes = bytearray(key,'utf8')
            value_bytes = bytearray(value,'utf8')
            print (topic_name, key, value_bytes)
            producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
            producer_instance.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def connect_kafka_producer(self):
        _producer = None
        try:
            _producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER], api_version=(0, 10))
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
        finally:
            return _producer

producer_object = kafka_producer()

class Data_Streamer():

    def __init__(self):
        self.start_time = datetime.now()

    def stream_data(self):
        producer_instance = producer_object.connect_kafka_producer()
        df = spark.read.parquet("data/streaming_data")
        df = df.withColumn("index", functions.monotonically_increasing_id())
        # count the number of rows in the DataFrame
        row_count = df.count()

        # use a for loop to iterate over all rows in the DataFrame
        for i in range(row_count):
            row = df.filter(functions.col("index") == i).collect()[0]
            # Convert the SparseVector to a dense numpy array
            dense_vector = np.array(row["independent_features"].toArray())

            # Convert the numpy array to a JSON string
            vector_string = json.dumps(dense_vector.tolist())

            # Publish the message
            producer_object.publish_message(producer_instance, "hackathon", "data", vector_string)
            time.sleep(5)

if __name__ == '__main__':
    data_producer_object = Data_Streamer()
    data_producer_object.stream_data()