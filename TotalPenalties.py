import pandas as pd
import numpy as np

df = pd.read_excel('horizonInputFileNew.xlsx')
underdraw = (df['underdraw']).values.tolist()
overdraw = (df['overdraw']).values.tolist()
deviation = []
under = []
over = []
for i in underdraw:
    if i > 200:
        i = 21
    under.append(i)
for j in overdraw:
    if j > 200:
        j = 21
    over.append(j)


# print("deviation: ", deviation)
# print("overdraw: ", overdraw)
# print("underdraw: ",underdraw)
df2 = pd.DataFrame.from_dict({'overdraw':over,'underdraw':under})
df2.to_excel('horizonInputFileNew.xlsx')