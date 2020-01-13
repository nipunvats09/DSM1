import pandas as pd
import numpy as np
df = pd.read_excel('fgg.xlsx')


actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()
# results = df['result'].values.tolis
dev = []
counts = []
plus_counter = 0
minus_counter = 0
row_counter = 0
answer_counter = 1
results = []
sustained = []

for i,j  in zip(actual, schedule):
    devs = i - j
    dev.append(devs)

for each in dev:

    if each > 0:
        minus_counter = 0
        plus_counter += 1

        if plus_counter == 7:
            count = answer_counter
            row_counter = answer_counter
            counts.append(count)
            plus_counter = 0
            answer_counter += 1
        else:
            counts.append(0)

    elif each < 0:
        plus_counter = 0
        minus_counter += 1

        if minus_counter == 7:
            count = answer_counter
            row_counter = answer_counter
            counts.append(count)
            minus_counter = 0
            answer_counter += 1

        else:
            counts.append(0)

    row_counter += 1

print("counter: ", counts)


# df.loc[(df['count'] >= 1) & (df['count'] <= 5) & (df['UI difference'] > 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.03
# df.loc[(df['count'] >= 1) & (df['count'] <= 5) & (df['UI difference'] < 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.03
#
# df.loc[(df['count'] >= 6) & (df['count'] <= 10) & (df['UI difference'] > 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.05
# df.loc[(df['count'] >= 6) & (df['count'] <= 10) & (df['UI difference'] < 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.05
#
# df.loc[(df['count'] > 10)  & (df['UI difference'] > 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.1
# df.loc[(df['count'] > 10)  & (df['UI difference'] < 0),'sustained'] = abs(df['UI difference']) * df['rate'] * 10 * 0.25 * 0.1
#
# df.loc['Total'] = pd.Series(df['sustained'].sum(), index = ['sustained'])
# df