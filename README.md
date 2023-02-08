# SEDS - Hackathon 2 - House Price Prediction

## Predict the House Price for New York Housing Dataset using PySpark. 

## Team name       - Group 13
## Team members - Aman Kumar, Krishnanand S H and Syed Asif

## Files:

  #### Dockerfile - Containerise the application
  #### House price prediction - training.ipynb - Model training and evaluation 
      ##### Template code is provided in the "House price prediction - training.ipynb" notebook file to install requirements, data cleaning and training. 
  #### House price prediction - test.ipynb - Fitting the model on test dataset
      ##### Template code is provided in the "House price prediction - test.ipynb" notebook file to test the model created on test data. 
  #### api.py - Publish the metrics and prediction output
  #### Data - You will also be required to use the included train.csv - Training dataset and test.csv - Test dataset file.
  #### train.csv - Training dataset
  #### test.csv - Test dataset
  #### Train_data_metrics.csv - Evaluation metrics of various machine learning models
  #### final_submission.csv - Final prediction of Sale Price values of the test data set 
  #### linearmodel - Trained Linear Regression model 
  #### rfmodel - Trained Random Forest Regression model 
  #### gbrmodel - Trained Gradiant Boost Regression model 
  #### generated_models - folder contains all the model generated during training
  #### kafka_2.13-2.8.2 - Local Kafka Installation
  #### config.yml - For configuration 
  #### Data_Producer.py - Kafka producer
  #### Dockerfile - To build docker container
  #### Initializer.py - Class to initialize Kafka producer and consumer
  #### Prediction_Consumer.py - Kafka consumer in which consumer is loaded to predict the House Price
  #### requirements.txt - List of packages to be installed thorugh pip
  #### spark-3.3.1-bin-hadoop2.tgz - Local installation of spark
  
  #### To build an docker image: docker build -t hackathon .
  #### To Run as container: docker run -p 9092:9092 -p 2181:2181 hackathon