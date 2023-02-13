## Predict the House Price for New York Housing Dataset using PySpark. 

  #### House price prediction - training.ipynb - Model training and evaluation. 
  [View on Kaggle](https://www.kaggle.com/syedasifmn/housing-price-prediction-training/)
  #### House price prediction - test.ipynb - Fitting the model on test dataset.
  [View on Kaggle](https://www.kaggle.com/syedasifmn/housing-price-prediction-test/)
  #### Data - Folder with all the .csv files.
  #### train.csv - Training dataset.
  #### test.csv - Test dataset.
  #### Train_data_metrics.csv - Evaluation metrics of trained machine learning models.
  #### final_prediction.csv - Final prediction of Sale Price values of the test data set. 
  #### generated_models - Folder containing the models generated during training.
  #### linearmodel - Trained Linear Regression model. 
  #### rfmodel - Trained Random Forest Regression model. 
  #### gbrmodel - Trained Gradiant Boost Regression model. 
  #### kafka_2.13-2.8.2 - Local Kafka Installation.
  #### config.yml - For Kafka Producer/Consumer configuration.
  #### Data_Producer.py - Kafka producer.
  #### Prediction_Consumer.py - Kafka consumer, which predicts sale price from the streamed features.
  #### Dockerfile - To containerize Kafka producer/consumer.
  #### docker-compose.yml - To configure your application’s services.
  #### Initializer.py - Class to initialize Kafka producer and consumer.
  #### requirements.txt - List of packages to be installed thorugh pip.
  #### spark-3.3.1-bin-hadoop2.tgz - Local installation of spark.
  
  ---------------------------------------
  #### To run: docker-compose up --build
  ---------------------------------------
