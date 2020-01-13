import pandas as pd
def fun(actual,schedule,df):
    underdraw = []
    overdraw = []
    for i,j, in zip(schedule, actual):
        dev = j - i
        if dev < 0:
            underdraw.append(dev)
        else:
            underdraw.append(0)

        if dev > 0:
            overdraw.append(dev)
        else:
            overdraw.append(0)

    df['underdraw'] = pd.Series(underdraw)
    df['overdraw'] = pd.Series(overdraw)
    df.to_excel('mainfile.xlsx')

    # writer = pd.ExcelWriter('newdev.xlsx', engine='xlsxwriter')
# df = df[["underdraw", "overdraw"]]  # the columns you want in the excel
# df.to_excel(writer, "SHEET_NAME", index=False)

