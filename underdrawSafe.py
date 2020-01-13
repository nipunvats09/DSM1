def underdraw(allowLowLimit, modelInput):
    cap = []
    capbe =[]
    penalties = []
    receivables = []

    # UNDERDRAW PENALTIES AND RECEIVABLES CALCULATIONS
    for i, j, k, q, l in zip(modelInput['frequency'], modelInput['deviations'], modelInput['LowerLimits'],
                             modelInput['results'], modelInput['ACP']):
        if k > allowLowLimit:
            if 0 > j >= -allowLowLimit and i < 50.05:
                cappedAmount = abs(j)
                Receivables = abs(j) * q * 2.5
                cap.append(cappedAmount)
                receivables.append(Receivables)
                # print('capped amount: ', cap)
                # print('receivables: ', rec)


            elif j < -allowLowLimit and i < 50.05:
                CappedAmountBeyondLimit = abs(j) - allowLowLimit
                capbe.append(CappedAmountBeyondLimit)
                Receivables = allowLowLimit * q * 2.5
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
                Receivables = allowLowLimit * q * 2.5
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

    UnderdrawOutput = {
        'receivables': receivables, 'penalties': penalties, 'SumRec': SumRec, 'SumPen': SumPen
                   }
    return UnderdrawOutput

    # print ("Total Receivables: ", SumRec)
    # print ("penalties: \n", penalties)
    # print ("Total Penalties: ", SumPen)
    # return penalties, receivables
    # df['receivables'] = pd.Series(receivables)
    # df['penalties'] = pd.Series(penalties)
    # df['Total receivables'] = pd.Series(SumRec)
    # df['Total penalties'] = pd.Series(SumPen)
    # df.to_excel('underdraw penalties 50MW 1hr.xlsx')




