import pandas as pd
import numpy as np
df = pd.read_excel('main input.xlsx')

interval = df['interval'].values.tolist()
actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()


for a in interval:
    day_counter = 1
    if a == "0:00":
        day_counter +=1

print(day_counter)
# print type(interval)