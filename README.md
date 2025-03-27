# 📈 Market Mood Detector

A Python project that detects stock market regimes (bullish, bearish, or neutral) using machine learning.

![Market Mood Visualization](https://i.imgur.com/JKvQxZa.png) *(example visualization)*

## 🌟 Features

- Classifies market conditions into 3 moods:
  - 🐂 Bullish (Happy Market)
  - 🐻 Bearish (Sad Market) 
  - 😴 Neutral (Sleepy Market)
- Uses K-Means clustering on price and volatility data
- Visualizes results with matplotlib
- Simple CSV data input format

## Install dependencies:

pip install -r requirements.txt

## Data Format

Date,Price,Volume
2023-01-01,100,1000
2023-01-02,102,1200

## Sample output

📊 Market Mood Report:
         Date  Price        Mood_Name
2  2023-01-03    105  Happy Market 🐂
3  2023-01-04    103   Sad Market 🐻
4  2023-01-05     98   Sad Market 🐻
