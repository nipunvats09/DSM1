def overdraw(allowLowLimit, allowMidLimit, allowHighLimit, modelInput):

    # CALCULTING OVERDRAW PENALTIES
    OverPenalties = []
    OverPenalties1 = []
    OverPenalties2 = []
    OverPenalties3 = []
    OverPenalties4 = []
    OverPenalties5 = []

    for i, j, k, o, l, m in zip(modelInput['deviations'], modelInput['LowerLimits'], modelInput['MidLimits']
            ,modelInput['HighLimits'], modelInput['results'], modelInput['frequency']):
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
    # print("Total overdraw penalties: ", Sum)

    OverdrawOutput = {
        'OverPenalties': OverPenalties, 'OverPenalties1': OverPenalties1,
                   'OverPenalties2': OverPenalties2, 'OverPenalties3': OverPenalties3,
                   'OverPenalties4': OverPenalties4, 'OverPenalties5': OverPenalties5,
                   'Sum': Sum
    }

    return OverdrawOutput

    # modelInput['modelData']['Penalty'] = Sum
    # modelData['if freq is below 49.85 Penalty'] = pd.Series(OverPenalties)
    # modelData['upto 12 Penalty'] = pd.Series(OverPenalties1)
    # modelData['12-15% Penalty'] = pd.Series(OverPenalties2)
    # modelData['15-20% Penalty'] = pd.Series(OverPenalties3)
    # modelData['above 20% Penalty'] = pd.Series(OverPenalties4)
    # modelData['if freq is above 50.05 Penalty'] = pd.Series(OverPenalties5)
    # modelData.to_excel('overdraw penalty 50MW 1hr.xlsx')
    # # modelData = modelData[["Penalty", ""]]  # the columns you want in the excel
    # modelData.to_excel(writer, "SHEET_NAME", index=False)



