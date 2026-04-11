from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StockPredictionSerializer
from rest_framework import status
from rest_framework.response import Response
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime
import os
from django.conf import settings
from .utils import save_plot
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model 
from sklearn.metrics import mean_squared_error,r2_score

# Create your views here.
class StockPredictionAPIView(APIView):
    def post(self,request):
        serializer = StockPredictionSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer.validated_data['ticker']

            # fetch the data from yfinance
            now = datetime.now()
            start = datetime(now.year-10,now.month, now.day)
            end = now
            df = yf.download(ticker,start,end)
            # print(df)
            if df.empty:
                return Response({"error": "No data found for this ticker.","status": status.HTTP_404_NOT_FOUND})

            df = df.reset_index()
            print(df)

            # Generate Basic Plot
            # matplotlib having 2 backends, one is for interactive and other is for non-interactive.
            # automated request to use the non-interactive backend.
            plt.switch_backend("AGG") # anti-grain geometry, non-interactive backend
            plt.figure(figsize=(12,5))
            plt.plot(df.Close,label="Close Price")
            plt.title(f"closing price of {ticker}")
            plt.xlabel("Days")
            plt.ylabel("Close Price")
            plt.legend()

            # Save the plot file
            plot_img_path = f"{ticker}_plot.png"
            plot_img = save_plot(plot_img_path)
            # print(plot_img)

            # 100 Days Moving Average
            ma100 = df.Close.rolling(100).mean()
            plt.switch_backend("AGG")
            plt.figure(figsize=(12,5))
            plt.plot(df.Close,label="Close Price")
            plt.plot(ma100,"r",label="100 DMA")
            plt.title(f"100 Days Moving Average of {ticker}")
            plt.xlabel("Days")
            plt.ylabel("Close Price")
            plt.legend()
            plot_img_path = f"{ticker}_100_dma.png"
            plot_100_dma = save_plot(plot_img_path)


            # 200 Days Moving Average
            ma200 = df.Close.rolling(200).mean()
            plt.switch_backend("AGG")
            plt.figure(figsize=(12,5))
            plt.plot(df.Close,label="Close Price")
            plt.plot(ma100,"r",label="100 DMA ")
            plt.plot(ma200,"g",label="200 DMA")
            plt.title(f"200 Days Moving Average of {ticker}")
            plt.xlabel("Days")
            plt.ylabel("Close Price")
            plt.legend()
            plot_img_path = f"{ticker}_200_dma.png"
            plot_200_dma = save_plot(plot_img_path)

            # 1. 70% of data for training
            # 2. 30% of data for testing
            data_training = pd.DataFrame(df.Close[0:int(len(df)*0.7)])
            data_testing = pd.DataFrame(df.Close[int(len(df)*0.7):len(df)])
            
            # Scaling training data into 0 and 1
            scaler = MinMaxScaler(feature_range=(0,1))

            # Load model 
            model = load_model("../Resources/stock_prediction_model.keras")

            # Preparing test data
            past_100_days = data_training.tail(100)
            final_df = pd.concat([past_100_days,data_testing], ignore_index=True)
            input_data = scaler.fit_transform(final_df)
            x_test = []
            y_test = []
            for i in range(100,input_data.shape[0]):
                x_test.append(input_data[i-100:i])
                y_test.append(input_data[i,0])
            x_test, y_test = np.array(x_test) , np.array(y_test)
            
            # Making Prediction
            y_predicted = model.predict(x_test)

            # Revert the scaled price to the original price
            y_predicted1 = scaler.inverse_transform(y_predicted.reshape(-1,1)).flatten()
            y_test1 = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()
            # print("y_predicted=> ",y_predicted1)
            # print("y_test=> ",y_test1)

            # Plot the Final Prediciton
            plt.switch_backend("AGG")
            plt.figure(figsize=(12,5))
            plt.plot(y_test1, "b",label="Original Price")
            plt.plot(y_predicted1,"r",label="Predicted Price")
            plt.title(f"Final Prediction of {ticker}")
            plt.xlabel("Days")
            plt.ylabel("Close Price")
            plt.legend()
            plot_img_path = f"{ticker}_final_prediction.png"
            plot_prediction = save_plot(plot_img_path)

            # Model Evaluation
            # Mean Squared Error 
            mse = mean_squared_error(y_test1, y_predicted1)
            # Root Means Squared error
            rmse = np.sqrt(mse)
            # R-Squared Score
            r2 = r2_score(y_test1, y_predicted1)

            return Response({"status": "success",
                             "plot_img" : plot_img,
                             "plot_100_dma" : plot_100_dma,
                             "plot_200_dma" : plot_200_dma,
                             "plot_prediction" : plot_prediction,
                             "mse": mse,
                             "rmse": rmse,  
                                "r2": r2
                             })