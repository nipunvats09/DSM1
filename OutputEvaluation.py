import pandas as pd
import numpy as np

def outputEval(modelInput, UnderdrawOutput, OverdrawOutput, SustainDevOutput):
    # SHOWING UNDERDRAW AND OVERDRAW
    modelInput['modelData']['Deviations'] = pd.Series(modelInput['deviations'])

    # EXPORTING UNDERDRAW RECEIVABLES AND PENALTIES TO EXCEL.
    modelInput['modelData']['Underdraw Recievables'] = pd.Series(UnderdrawOutput['receivables'])
    modelInput['modelData']['Underdraw Penalties'] = pd.Series(UnderdrawOutput['penalties'])

    # EXPORTING OVERDRAW PENALTIES TO EXCEL
    modelInput['modelData']['Overdraw penalties for frequency below 49.85Hz'] = pd.Series(OverdrawOutput['OverPenalties'])
    modelInput['modelData']['Overdraw penalties for DSM'] = pd.Series(OverdrawOutput['OverPenalties1'])
    modelInput['modelData']['Overdraw penalties for ADSM 12%-15%'] = pd.Series(OverdrawOutput['OverPenalties2'])
    modelInput['modelData']['Overdraw penalties for ADSM 15%-20%'] = pd.Series(OverdrawOutput['OverPenalties3'])
    modelInput['modelData']['Overdraw penalties for ADSM above 20%'] = pd.Series(OverdrawOutput['OverPenalties4'])
    modelInput['modelData']['Overdraw penalties for frequency above 50.05'] = pd.Series(OverdrawOutput['OverPenalties5'])

    # ADDITION OF ALL PENALTIES AND SUBTRACTING RECEIVABLES
    Total = []
    for over1, over2, over3, over4, over5, under1, sustain, under2 in zip(OverdrawOutput['OverPenalties'], OverdrawOutput['OverPenalties'],
                                                                  OverdrawOutput['OverPenalties'], OverdrawOutput['OverPenalties'],
                                                                  OverdrawOutput['OverPenalties'], UnderdrawOutput['penalties'],
                                                                          SustainDevOutput['sustained'], UnderdrawOutput['receivables']):
        total = (over1+over2+over3+over4+over5+under1+sustain) - under2
        Total.append(total)

    # EXPORTING SUSTAINED DEVIATION PENALTIES
    modelInput['modelData']['Counter'] = pd.Series(SustainDevOutput['result'])
    modelInput['modelData']['Sustain Deviation Penalties'] = pd.Series(SustainDevOutput['sustained'])

    # EXPORTING TOTAL PENALTIES AND RECIEVABLES TO EXCEL
    modelInput['modelData']['Total'] = pd.Series(Total)

    # EXCEL SHEET WRITER
    writer = pd.ExcelWriter("DSM with storage 30MW 1Hr updated.xlsx", engine='xlsxwriter')
    modelInput['modelData'].to_excel(writer, sheet_name='penalties and receivables', startrow=1, header=False)

    workbook = writer.book
    worksheet = writer.sheets['penalties and receivables']

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'border': 1
    })

    for col_num, values in enumerate(modelInput['modelData'].columns.values):
        worksheet.write(0, col_num+1,values,header_format)

    writer.save()