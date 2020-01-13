import pandas as pd
df = pd.read_excel('new delhi.xlsx')
acp = float(input())
df.loc[df['frequency'] >= 50.05, 'rate'] = 0
df.loc[(df['frequency'] < 50.05) & (df['frequency'] >= 50.04), 'rate'] = acp * 0.2
df.loc[(df['frequency'] < 50.04) & (df['frequency'] >= 50.03), 'rate'] = acp * 0.4
df.loc[(df['frequency'] < 50.03) & (df['frequency'] >= 50.02), 'rate'] = acp * 0.6
df.loc[(df['frequency'] < 50.02) & (df['frequency'] >= 50.01), 'rate'] = acp * 0.8
df.loc[(df['frequency'] < 50.01) & (df['frequency'] >= 50.00), 'rate'] = acp
df.loc[(df['frequency'] < 50.00) & (df['frequency'] >= 49.99), 'rate'] = 50 + 15 * acp / 16
df.loc[(df['frequency'] < 49.99) & (df['frequency'] >= 49.98), 'rate'] = 100 + 14 * acp / 16
df.loc[(df['frequency'] < 49.98) & (df['frequency'] >= 49.97), 'rate'] = 150 + 13 * acp / 16
df.loc[(df['frequency'] < 49.97) & (df['frequency'] >= 49.96), 'rate'] = 200 + 12 * acp / 16
df.loc[(df['frequency'] < 49.96) & (df['frequency'] >= 49.95), 'rate'] = 250 + 11 * acp / 16
df.loc[(df['frequency'] < 49.95) & (df['frequency'] >= 49.94), 'rate'] = 300 + 10 * acp / 16
df.loc[(df['frequency'] < 49.94) & (df['frequency'] >= 49.93), 'rate'] = 350 + 9 * acp / 16
df.loc[(df['frequency'] < 49.93) & (df['frequency'] >= 49.92), 'rate'] = 400 + 8 * acp / 16
df.loc[(df['frequency'] < 49.92) & (df['frequency'] >= 49.91), 'rate'] = 450 + 7 * acp / 16
df.loc[(df['frequency'] < 49.91) & (df['frequency'] >= 49.90), 'rate'] = 500 + 6 * acp / 16
df.loc[(df['frequency'] < 49.90) & (df['frequency'] >= 49.89), 'rate'] = 550 + 5 * acp / 16
df.loc[(df['frequency'] < 49.89) & (df['frequency'] >= 49.88), 'rate'] = 600 + 4 * acp / 16
df.loc[(df['frequency'] < 49.88) & (df['frequency'] >= 49.87), 'rate'] = 650 + 3 * acp / 16
df.loc[(df['frequency'] < 49.87) & (df['frequency'] >= 49.86), 'rate'] = 700 + 2 * acp / 16
df.loc[(df['frequency'] < 49.86) & (df['frequency'] >= 49.85), 'rate'] = 750 + acp / 16
df.loc[(df['frequency'] < 49.85), 'rate'] = 800
df.to_excel('dsm rate.xlsx')
df.head()


# to calculate unschedule interchange
df['UI'] = ((df['Delhi Actual'] - df['Delhi Schedule'])/df['Delhi Schedule']) * 100
df.head()


ACP = input("enter the ACP value: ")

# calculating UNDERDRAW
# if the frequency is below or equal to 50.05hz and unschedule interchange is below 12%
df.loc[(df['UI'] >= -12 ) & (df['UI'] < 0 ) & (df['frequency'] <= 50.05), 'capping'] = 12 - abs(df['UI'])
df.loc[(df['UI'] >= -12 ) & (df['UI'] < 0 ) & (df['frequency'] <= 50.05), 'amount recieved'] = abs(df['capping'] * df['UI'] * 10 * 0.25)

# if the frequency is above 50.05hz
df.loc[(df['frequency'] > 50.05), 'penalty'] = abs(df['UI'] * ACP * 10 * 0.25)
df




# calculating overdraw
# if the frequency is below 49.85hz and unschedule interchange is below 12%
df.loc[(df['UI'] > 0) & (df['frequency'] < 49.85), 'overdraw penalty'] = abs(df['UI']) * 2 * df['rate']

# # if the frequency is between 49.85hz and 50.05 and unschedule interchange is below or equal 12%
df.loc[(df['UI'] > 0) & (df['UI'] <= 12 ) & (df['frequency'] >= 49.85) & (df['frequency'] < 50.05), 'overdraw penalty for 12%'] = df['UI'] * df['rate']


# if the frequency is between 49.85hz and 50.05 and unschedule interchange is between 12% to 15%
df.loc[(df['UI'] > 12) & (df['UI'] <= 15 ) & (df['frequency'] >= 49.85) & (df['frequency'] < 50.05), 'overdraw penalty for 15%'] = (df['UI'] - 12) * 13.2 * df['rate']


# if the frequency is between 49.85hz and 50.05 and unschedule interchange is between 15% to 20%
df.loc[(df['UI'] > 15) & (df['UI'] <= 20 ) & (df['frequency'] >= 49.85) & (df['frequency'] < 50.05), 'overdraw penalty for 20%'] = (df['UI'] - 15) * 17.6 * df['rate']


# if the frequency is between 49.85hz and 50.05 and unschedule interchange is above 20%
df.loc[(df['UI'] > 20) & (df['frequency'] >= 49.85) & (df['frequency'] < 50.05), 'overdraw penalty for above 20%'] =  (df['UI'] - 20) * 24.6 * df['rate']


# if the frequency is above 50.05hz and unschedule interchange is also above zero
df.loc[(df['frequency'] > 50.05), 'overdraw penalty'] = 0
df.to_excel('final.xlsx')
df


# sustained deviations
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
