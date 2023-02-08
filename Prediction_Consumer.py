import os
from kafka import KafkaConsumer, KafkaProducer
from Initializer import Initialize
import json
import pickle
import numpy as np
from pyspark.ml.regression import RandomForestRegressionModel
from pyspark.sql import DataFrame, SparkSession
import pandas as pd
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

init_object = Initialize()
spark = SparkSession.builder.appName("House Price Prediction").getOrCreate()
KAFKA_BROKER = os.getenv("KAFKA_BROKER")

class Prediction_Consumer():
    
    def predict_prize(self,features):
        predicted_cost = rf_model.transform(features)
        return predicted_cost
    
    def gather_data(self):
        consumer = KafkaConsumer(auto_offset_reset='latest',
                                 bootstrap_servers=[KAFKA_BROKER], api_version=(0, 10),
                                 consumer_timeout_ms=1000)

        consumer.subscribe(topics=['hackathon'])  # Subscribe to a pattern

        while True:
            for message in consumer:
                if message.topic == "hackathon":
                    value = (message.value.decode())
                    value = value.replace("[", "").replace("]", "")
                    string_list = value.split(",")
                    double_list = [float(x) for x in string_list]
                    int_list = [int(x) for x in double_list]
                    rdd = spark.sparkContext.parallelize([int_list])
                    df = rdd.toDF(["values"])

                    # Create an instance of the VectorAssembler
                    assembler = VectorAssembler(inputCols=["values"], outputCol="independent_features")

                    # Use the VectorAssembler to convert the column to the required type
                    df = assembler.transform(df)
                    
                    predicted_cost = self.predict_prize(df)
                    print ("Predicted Cost: ", predicted_cost.select("prediction"))
                    

if __name__ == '__main__':
    rf_model = RandomForestRegressionModel.load("generated_models/rfmodel")
    pred_consumer = Prediction_Consumer()
    pred_consumer.gather_data()