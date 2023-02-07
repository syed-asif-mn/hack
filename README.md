# SEDS - Hackathon 2 - House Price Prediction

## Predict the House Price for New York Housing Dataset using PySpark. 

## Team name       - Group 13
## Team members - Aman Kumar, Krishnanand S H and Syed Asif

## Files:

  #### Dockerfile - Containerise the application
  #### House price prediction - training.ipynb - Model training and evaluation 
  #### House price prediction - test.ipynb - Fitting the model on test dataset
  #### Data - Folder with all the csv and streaming data files.
  #### train.csv - Training dataset
  #### test.csv - Test dataset
  #### synthesized_data - User Generated data
  #### train_data_metrics.csv - Evaluation metrics of various machine learning models
  #### final_predictions.csv - Final prediction of Sale Price values of the test data set 
  #### linearmodel - Trained Linear Regression model 
  #### rfmodel - Trained Random Forest Regression model 
  #### gbrmodel - Trained Gradiant Boost Regression model 
  #### generated_models - folder contains all the model generated during training
  #### kafka_2.13-2.8.2 - Local Kafka Installation
  #### config.yml - Used to configure kafka producer/consumer
  #### Data_Producer.py - Kafka producer
  #### Dockerfile - To build docker container
  #### docker-compose.yml - To configure and run multi-container Docker services
  #### Initializer.py - Class to initialize Kafka producer and consumer
  #### Prediction_Consumer.py - Kafka consumer in which consumer is loaded to predict the House Price
  #### requirements.txt - List of packages to be installed thorugh pip
  #### spark-3.3.1-bin-hadoop2.tgz - Local installation of spark

  #### To Build and Run: docker-compose up --build