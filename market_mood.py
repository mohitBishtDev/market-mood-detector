# Import our magic tools
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Read our stock data
print("📖 Reading stock data...")
data = pd.read_csv('data/stock_data.csv')

# 2. Calculate daily changes and volatility
print("🧮 Calculating mood signals...")
data['Daily_Change'] = data['Price'].pct_change() * 100  # Percentage change
data['Volatility'] = data['Daily_Change'].rolling(3).std()  # 3-day volatility

# Remove the first few days with no data
data = data.dropna()

# 3. Prepare data for our mood detector
X = data[['Daily_Change', 'Volatility']]

# 4. Train our mood detector (3 moods: happy, sad, sleepy)
print("🤖 Training mood detector...")
kmeans = KMeans(n_clusters=3, random_state=42)
data['Mood'] = kmeans.fit_predict(X)

# 5. Name our moods
mood_names = {
    0: 'Sleepy Market 😴',
    1: 'Happy Market 🐂',
    2: 'Sad Market 🐻'
}
data['Mood_Name'] = data['Mood'].map(mood_names)

# 6. Show our results
print("\n📊 Market Mood Report:")
print(data[['Date', 'Price', 'Mood_Name']])

# 7. Make a pretty picture
colors = ['gray', 'green', 'red']
for mood, color in zip(range(3), colors):
    mood_data = data[data['Mood'] == mood]
    plt.scatter(mood_data['Daily_Change'], mood_data['Volatility'], 
               c=color, label=mood_names[mood])

plt.xlabel('Daily Change (%)')
plt.ylabel('Volatility')
plt.title('Market Mood Detection')
plt.legend()
plt.grid(True)
plt.show()

print("\nAll done! 🎉 Check out the picture to see market moods!")