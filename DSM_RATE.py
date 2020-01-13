import pandas as pd
df = pd.read_excel('fgg.xlsx')

# DSM rate calculations for different frequency slots(21 to be exact)
df = pd.read_excel('fgg.xlsx')
actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()
results = []

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

# print results
df['dsm rate'] = pd.Series(results)
df.to_excel('dsm rate.xlsx')