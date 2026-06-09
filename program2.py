import pandas as pd

data = pd.read_csv('orders.csv')
# print(len(data))

# app = 0
# website = 0
# mobile = 0

# for i in data["channel"]:
#     if i =="Mobile Web":
#         mobile = mobile +1

avgs = data["total_amount"].mean()
print(avgs)

belowavg = 0

for i in data["total_amount"]:
    if i > avgs:
     belowavg = belowavg + 1

print(belowavg)

