import plotly.express as px
import csv
import pandas as pd

df = pd.read_csv("main.csv")
score = df["TOEFL Score"].tolist()
chance = df["Chance of Admit "].tolist()

import numpy as np
score = np.array(score)
chance = np.array(chance)
m,b = np.polyfit(score,chance,1)

y = []
for x in score:
  y_value = (m * x) + b
  y.append(y_value)
fig = px.scatter(x = score, y = chance)
fig.update_layout(shapes = [
                            dict(
                                type = "line",
                                 y0 = min(y),
                                 y1 = max(y),
                                 x0 = min(score),
                                 x1 = max(score)
                            )
])   
fig.show()

x = 100
y = (m * x) + b
print(f"Chance of someone with score {x} is {y}")

