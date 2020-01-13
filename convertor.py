import pandas as pd
import numpy as np
from datetime import datetime, date

df = pd.read_excel('testyl.xlsx')

time = np.array(df['Date'])
actual = np.array(df['actual'])
schedule = np.array(df['schedule'])
freq = np.array(df['frequency'])
ACP = np.array(df['acp'])
dev = []
counts = []
plus_counter = 0
minus_counter = 0
row_counter = 0
answer_counter = 1
results = []
sustained = []
sustained1 = []

for i,j  in zip(actual, schedule):
    devs = i - j
    dev.append(devs)

# for DSM rate
# DSM RATE CALCULATOR
for each, acp in zip(freq, ACP):
    if each >= 50.05:
        rate = 0
        results.append(rate)
    elif each < 50.05 and each >= 50.04:
        rate = acp * 0.2
        results.append(rate)
    elif each < 50.04 and each >= 50.03:
        rate = acp * 0.4
        results.append(rate)
    elif each < 50.03 and each >= 50.02:
        rate = acp * 0.6
        results.append(rate)
    elif each < 50.02 and each >= 50.01:
        rate = acp * 0.8
        results.append(rate)
    elif each < 50.01 and each >= 50.00:
        rate = acp
        results.append(rate)
    elif each < 50.00 and each >= 49.99:
        rate = 50 + 15 * acp / 16
        results.append(rate)
    elif each < 49.99 and each >= 49.98:
        rate = 100 + 14 * acp / 16
        results.append(rate)
    elif each < 49.98 and each >= 49.97:
        rate = 150 + 13 * acp / 16
        results.append(rate)
    elif each < 49.97 and each >= 49.96:
        rate = 200 + 12 * acp / 16
        results.append(rate)
    elif each < 49.96 and each >= 49.95:
        rate = 250 + 11 * acp / 16
        results.append(rate)
    elif each < 49.95 and each >= 49.94:
        rate = 300 + 10 * acp / 16
        results.append(rate)
    elif each < 49.94 and each >= 49.93:
        rate = 350 + 9 * acp / 16
        results.append(rate)
    elif each < 49.93 and each >= 49.92:
        rate = 400 + 8 * acp / 16
        results.append(rate)
    elif each < 49.92 and each >= 49.91:
        rate = 450 + 7 * acp / 16
        results.append(rate)
    elif each < 49.91 and each >= 49.90:
        rate = 500 + 6 * acp / 16
        results.append(rate)
    elif each < 49.90 and each >= 49.89:
        rate = 550 + 5 * acp / 16
        results.append(rate)
    elif each < 49.89 and each >= 49.88:
        rate = 600 + 4 * acp / 16
        results.append(rate)
    elif each < 49.88 and each >= 49.87:
        rate = 650 + 3 * acp / 16
        results.append(rate)
    elif each < 49.87 and each >= 49.86:
        rate = 700 + 2 * acp / 16
        results.append(rate)
    elif each < 49.86 and each >= 49.85:
        rate = 750 + acp / 16
        results.append(rate)
    elif each < 49.85:
        rate = 800
        results.append(rate)

# SUSTAINED DEVIATION CALCULATOR
tes = []
# COUNTER RESETER FOR EVERY NEW DAY
for i,j, each in zip(time[0::],time[1::], dev): # comparing two days
    if i == j: #if they are equal increase the sustained deviation counter
        te = True
        tes.append(te)

        if each > 0:
            minus_counter = 0 #-(ve) deviation counter
            plus_counter += 1 #+(ve) deviation counter
            if plus_counter == 7: #checking the continuty for consecutive 7 positive deviations
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

            if minus_counter == 7: #checking the continuty for consecutive 7 negative deviations
                count = answer_counter
                row_counter = answer_counter
                counts.append(count)
                minus_counter = 0
                answer_counter += 1
            else:
                counts.append(0)

        row_counter += 1
    else:
        te = False
        tes.append(te)

        plus_counter = 0
        minus_counter = 0
        row_counter = 0
        answer_counter = 1




for i, j, k in zip(counts, dev, results):
    if 0 < i <= 5:
        if j > 0:
            sus = abs(j) * k * 0.075
            sustained.append(sus)


        if j < 0:
            sus = abs(j) * k * 0.075
            sustained.append(sus)

    elif 5 < i <= 10:
        if j > 0:
            sus = abs(j) * k * 0.125
            sustained.append(sus)

        if j < 0:
            sus = abs(j) * k * 0.125
            sustained.append(sus)

    elif i > 10:
        if j > 0:
            sus = abs(j) * k * 0.25
            sustained.append(sus)

        if j < 0:
            sus = abs(j) * k * 0.25
            sustained.append(sus)

    else:
        sustained.append(0)
SusSum = sum(sustained)
print(SusSum)
# print("counter: ",counts)
df['counter'] = pd.Series(counts)
df['sustain dev'] = pd.Series(sustained)
df['test'] = pd.Series(tes)
df.to_excel("sustained dev4.xlsx")


# print counts
# print sustained
# # SusSum = sum(sustained)
# # print(sustained)