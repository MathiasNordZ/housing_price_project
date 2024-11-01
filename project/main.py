import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/mathiasnord/Desktop/housing_price_project/project/dataset/Housing.csv")

plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 1], df.iloc[:, 0], alpha = 0.5)
plt.title("Housing price vs area")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.grid(True)
plt.show()

