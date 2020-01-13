def sustainDeviation(modelInput):
    sustained = []
    sustained1 = []
    nths = 96
    sequential_limit = 7
    sequential_count = sequential_finds = 0
    indexer = sequential_limit - 1
    sequential_list = [0 for _ in range(indexer)]
    skip = 0

    for index, num in enumerate(modelInput['deviations'][indexer:], indexer):
        result = 0
        if index % nths == 0:
            sequential_count = sequential_finds = 0
            skip = indexer
        if skip:
            skip -= 1
        else:
            negative = sum(1 for next_num in modelInput['deviations'][index - indexer:index + 1] if next_num < 0)
            positive = sum(1 for next_num in modelInput['deviations'][index - indexer:index + 1] if next_num >= 0)
            if sequential_limit in (positive, negative):
                sequential_finds += 1
                sequential_count = 0
                skip = indexer
                result = sequential_finds
        sequential_list.append(result)


    for i, j, k in zip(sequential_list, modelInput['deviations'], modelInput['results']):
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
    print(sustained)
    # print(sustained1)
    print(SusSum)
    print("counter: ",sequential_list)
    df['counter'] = pd.Series(sequential_list)
    df['sustain dev'] = pd.Series(sustained)

    df.to_excel("sustained dev 2020.xlsx")



