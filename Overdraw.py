import pandas as pd

df = pd.read_excel('main input.xlsx')
actual = df['actual'].values.tolist()
schedule = df['schedule'].values.tolist()
freq = df['frequency'].values.tolist()
ACP = df['acp'].values.tolist()
# results = df['dsm'].values.tolist()
# df = pd.read_excel('inputt.xlsx')
deviations = []
LowerLimits = []
MidLimits = []
HighLimits = []
results = []
OverPenalties = []
OverPenalties1 = []
OverPenalties2 = []
OverPenalties3 = []
OverPenalties4 = []
OverPenalties5 = []

allowLowLimit = float(input("enter the allowed lower limit: "))
allowMidLimit = float(input("enter the allowed mid limit: "))
allowHighLimit = float(input("enter the allowed high limit: "))
def overdraw():


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


    # DEVIATIONS AND LIMITS CALCULATOR
    for i, j in zip(actual, schedule):
        deviation = i - j
        deviations.append(deviation)
        # return deviations
    # print('deviation is : \n', deviations)
    for each in schedule:
        LowerLimit = each * 0.12
        LowerLimits.append(LowerLimit)
        MidLimit = each * 0.15
        MidLimits.append(MidLimit)
        HighLimit = each * 0.2
        HighLimits.append(HighLimit)
    # print(LowerLimits)
    # print(MidLimits)
    # print(HighLimits)


    # CALCULTING OVERDRAW PENALTIES
    for i, j, k, o, l, m in zip(deviations, LowerLimits, MidLimits, HighLimits, results, freq):
        if allowLowLimit < j:
            # if the frequency is below 49.85hz
            if i > 0 and m < 49.85:
                OverPenalty = i * l * 5
                OverPenalties.append(OverPenalty)
            else:
                OverPenalties.append(0)

            #  CALCULATING DSM FOR BELOW 12%
            if 0 < i <= allowLowLimit and 49.85 <= m < 50.05:
                OverPenalty1 = i * l * 2.5
                OverPenalties1.append(OverPenalty1)
            else:
                OverPenalties1.append(0)

            # CALCULATING ADSM FOR 12% TO 15%
            if allowLowLimit < i <= allowMidLimit and 49.85 <= m < 50.05:
                OverPenalty2 = (i * l * 2.5) + ((i - allowLowLimit) * l * 2.5 * 0.2)
                OverPenalties2.append(OverPenalty2)
            else:
                OverPenalties2.append(0)

            #  CALCULATING ADSM FOR 15% TO 20%
            if allowMidLimit < i <= allowHighLimit and 49.85 <= m < 50.05:
                OverPenalty3 = (i * l * 2.5) + ((allowMidLimit - allowLowLimit) * l * 2.5 * 0.2) + ((i - allowMidLimit)*l*2.5*0.4)
                OverPenalties3.append(OverPenalty3)
            else:
                OverPenalties3.append(0)

            #  CALCULATING ADSM FOR ABOVE 20%
            if allowHighLimit < i  and 49.85 <= m < 50.05:
                OverPenalty4 = (i * l * 2.5) + ((allowMidLimit - allowLowLimit) * l * 2.5 * 0.2) + ((allowHighLimit - allowMidLimit)* l * 2.5 * 0.4) + ((i - allowHighLimit)* l * 2.5 )
                OverPenalties4.append(OverPenalty4)
            else:
                OverPenalties4.append(0)

            # IF FREQUENCY IS ABOVE 50.05 THEN THERE IS NO PENALTY
            if i > 0 and m >= 50.05:
                OverPenalties5.append(0)
            else:
                OverPenalties5.append(0)

        else:
            # if the frequency is below 49.85hz
            if i > 0 and m < 49.85:
                OverPenalty = i * l * 5
                OverPenalties.append(OverPenalty)
            else:
                OverPenalties.append(0)

            #  CALCULATING DSM FOR BELOW 12% OVERDRAW
            if 0 < i <= j and 49.85 <= m < 50.05:
                OverPenalty1 = i * l * 2.5
                OverPenalties1.append(OverPenalty1)
            else:
                OverPenalties1.append(0)

            # CALCULATING ADSM FOR 12% TO 15% OVERDRAW
            if j < i <= k and 49.85 <= m < 50.05:
                OverPenalty2 = (i * l * 2.5) + ((i - j) * l * 2.5 * 0.2)
                OverPenalties2.append(OverPenalty2)
            else:
                OverPenalties2.append(0)

            #  CALCULATING ADSM FOR 15% TO 20% OVERDRAW
            if k < i <= o and 49.85 <= m < 50.05:
                OverPenalty3 = (i * l * 2.5) + ((k - j) * l * 2.5 * 0.2) + ((i - k) * l * 2.5 * 0.4)
                OverPenalties3.append(OverPenalty3)
            else:
                OverPenalties3.append(0)

            #  CALCULATING ADSM FOR ABOVE 20% OVERDRAW
            if o < i and 49.85 <= m < 50.05:
                OverPenalty4 = (i * l * 2.5) + ((k - j) * l * 2.5 * 0.2) + ((o - k) * l * 2.5 * 0.4) + ((i - o) * l * 2.5 )
                OverPenalties4.append(OverPenalty4)
            else:
                OverPenalties4.append(0)

            # IF FREQUENCY IS ABOVE 50.05 THEN THERE IS NO PENALTY
            if i > 0 and m >= 50.05:
                OverPenalties5.append(0)
            else:
                OverPenalties5.append(0)


    Sum1 = sum(OverPenalties)
    Sum2 = sum(OverPenalties1)
    Sum3 = sum(OverPenalties2)
    Sum4 = sum(OverPenalties3)
    Sum5 = sum(OverPenalties4)
    Sum6 = sum(OverPenalties5)
    Sum = Sum1 + Sum2 + Sum3 + Sum4 + Sum5 + Sum6
    # print("Overdraw penalties for frequency below 49.85 : ", OverPenalties)
    # print("Overdraw penalties for upto 12% overdraw: ", OverPenalties1)
    # print("Overdraw penalties for between 12% to 15% overdraw: ", OverPenalties2)
    # print("Overdraw penalties for between 15% to 20% overdraw: ", OverPenalties3)
    # print("Overdraw penalties for above 20% overdraw : ", OverPenalties4)
    # print("Overdraw penalties for frequency above 50.05 : ", OverPenalties5)
    print("Total overdraw penalties: ", Sum)
    df['Penalty'] = Sum
    df['if freq is below 49.85 Penalty'] = pd.Series(OverPenalties)
    df['upto 12 Penalty'] = pd.Series(OverPenalties1)
    df['12-15% Penalty'] = pd.Series(OverPenalties2)
    df['15-20% Penalty'] = pd.Series(OverPenalties3)
    df['above 20% Penalty'] = pd.Series(OverPenalties4)
    df['if freq is above 50.05 Penalty'] = pd.Series(OverPenalties5)
    df.to_excel('overdraw penalty 50MW 1hr.xlsx')
    # # df = df[["Penalty", ""]]  # the columns you want in the excel
    # df.to_excel(writer, "SHEET_NAME", index=False)
    # writer.save()

overdraw()

