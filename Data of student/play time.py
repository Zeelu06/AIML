import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv("Data of student/students (1).csv")
y = df["result_percentage"]
X = df[["sleep_time"]]
sleep_model = LinearRegression()
sleep_model.fit(X, y)
print("Sleep Model:")