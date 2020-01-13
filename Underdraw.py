import pandas as pd
import numpy as np

df = pd.read_excel('input.xlsx')
actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()
deviations = []
LowerLimits = []
MidLimits = []
HighLimits = []
results = []
sustained = []
getInputs()
# cap = []
#
# capbe = []

df = pd.read_excel('main input.xlsx')
actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()
# results = df['dsm'].values.tolist()


# def dev():
#     deviations = []
#     LowerLimits = []
#     MidLimits = []
#     HighLimits = []
#     for i, j in zip(actual, schedule):
#         deviation = i - j
#         deviations.append(deviation)
#         return deviations
#     # print('deviation is : \n', deviations)
#     for each in schedule:
#         LowerLimit = each * 0.12
#         LowerLimits.append(LowerLimit)
#         MidLimit = each * 0.15
#         MidLimits.append(MidLimit)
#         HighLimit = each * 0.2
#         HighLimits.append(HighLimit)
#     # print('Lower limit: \n', LowerLimits)
#     # print('Mid limit: \n', MidLimits)
#     # print('High limit: \n', HighLimits)
#         return LowerLimits, MidLimits, HighLimits
def underdraw(modelinput):
    deviations = []
    LowerLimits = []
    MidLimits = []
    HighLimits = []
    results = []
    penalties = []
    receivables = []
    allowerLowLimit = float(input("enter the allowed limit: "))

    #DEVIATIONS AND LIMITS CALCULATOR

    for i, j in zip(actual, schedule):
        deviation = i - j
        deviations.append(deviation)
        # return deviations
    # print('deviation is : \n', deviations)
    for each in schedule:
        LowerLimit = each * 0.12
        LowerLimits.append(LowerLimit)
        # MidLimit = each * 0.15
        # MidLimits.append(MidLimit)
        # HighLimit = each * 0.2
        # HighLimits.append(HighLimit)
    # print(LowerLimits)


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
    # return results

    # UNDERDRAW PENALTIES AND RECEIVABLES CALCULATIONS

    for i, j, k, q, l in zip(freq, deviations, LowerLimits, results, ACP):
        if k > allowerLowLimit:
            if 0 > j >= -allowerLowLimit and i < 50.05:
                cappedAmount = abs(j)
                Receivables = abs(j) * q * 2.5
                cap.append(cappedAmount)
                receivables.append(Receivables)
                # print('capped amount: ', cap)
                # print('receivables: ', rec)


            elif j < -allowerLowLimit and i < 50.05:
                CappedAmountBeyondLimit = abs(j) - allowerLowLimit
                capbe.append(CappedAmountBeyondLimit)
                Receivables = allowerLowLimit * q * 2.5
                receivables.append(Receivables)
                # print('cappppp: ', capbe)
            else:
                receivables.append(0)
        else:
            if 0 > j >= -k and i <= 50.05:
                cappedAmount = abs(j)
                Receivables = abs(j) * q * 2.5
                cap.append(cappedAmount)
                receivables.append(Receivables)
                # print('capped amount: ', cap)
                # print('receivables: ', rec)

            elif j < -k and i < 50.05:
                CappedAmountBeyondLimit = abs(j) - k
                capbe.append(CappedAmountBeyondLimit)
                # print('cappppp: ', capbe)
                Receivables = allowerLowLimit * q * 2.5
                receivables.append(Receivables)

            else:
                receivables.append(0)


        if j < 0 and i >= 50.05:
            penalty = abs(j*l*2.5)
            penalties.append(penalty)
            # print("penalty: ", penalties)
        else:
            penalties.append(0)

    SumRec = sum(receivables)
    SumPen = sum(penalties)
    # print ("receivables: \n", receivables)
    print ("Total Receivables: ", SumRec)
    # print ("penalties: \n", penalties)
    print ("Total Penalties: ", SumPen)
    # return penalties, receivables
    df['receivables'] = pd.Series(receivables)
    df['penalties'] = pd.Series(penalties)
    df['Total receivables'] = pd.Series(SumRec)
    df['Total penalties'] = pd.Series(SumPen)
    df.to_excel('underdraw penalties 50MW 1hr.xlsx')



underdraw()
