import os
from kafka import KafkaConsumer, KafkaProducer
from Initializer import Initialize
import json
import pickle
import numpy as np
from pyspark.ml.regression import RandomForestRegressionModel
from pyspark.sql import DataFrame, SparkSession

init_object = Initialize()
spark = SparkSession.builder.appName("House Price Prediction").getOrCreate()
KAFKA_BROKER = os.getenv("KAFKA_BROKER")

class Prediction_Consumer():
    
    def predict_prize(self, features):
        print(features)
        predicted_cost = rf_model.predict(features)
        return predicted_cost[0][0]

    def gather_data(self):
        consumer = KafkaConsumer(auto_offset_reset='latest',
                                 bootstrap_servers=[KAFKA_BROKER], api_version=(0, 10),
                                 consumer_timeout_ms=1000)

        consumer.subscribe(topics=['hackathon'])  # Subscribe to a pattern

        while True:
            for message in consumer:
                if message.topic == "hackathon":
                    value_bytes = (message.value.decode())
                    print("Received Message: ")
                    print(value_bytes)
                    dense_vector_list = json.loads(value_bytes)
                    dense_vector = np.array(dense_vector_list).reshape((-1, 1))
                    predicted_cost = self.predict_prize(dense_vector)
                    print ("Predicted Cost: ", predicted_cost)

if __name__ == '__main__':
    pred_consumer = Prediction_Consumer()
    pred_consumer.gather_data()
    rf_model = RandomForestRegressionModel.load("generated_models/rfmodel")