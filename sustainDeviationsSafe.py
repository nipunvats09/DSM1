import pandas as pd
import numpy as np
from collections import deque

def sustainDeviation(modelInput):
    # df = pd.read_excel('main input.xlsx')
    sustained = []
    sustained1 = []
    chunk_size = 96  # nths
    sequential_limit = 7
    mode = 2

    def equal_sign(a, b):
        '''equal_sign returns true if both input parameters have the same sign'''
        if a == 0 and b == 0:
            return True
        if a > 0 and b > 0:
            return True
        if a < 0 and b < 0:
            return True
        return False

    def same_sign(items):
        '''same_sign returns true if every item shares the same sign'''
        # Special case for lengths 0 or 1 as they will never have different signs
        if len(items) < 2:
            return True
        # Check every item with the first one
        for i in range(1, len(items)):
            # If any of the items is different we can return False
            if not equal_sign(items[0], items[i]):
                return False
        # If we reach here they all have the same sign
        return True

    # The outter loop will be in charge of splitting the different chunks in the dataset.
    result = []
    chunk_start = 0
    # values is a circular buffer that will hold the previous and current values
    values = deque(maxlen=sequential_limit)
    while chunk_start < len(modelInput['deviations']):
        # Chunks end at the specified size or the maximum dataset length, preventing IndexErrors
        chunk_end = min(chunk_start + chunk_size, len(modelInput['deviations']))
        sequential_finds = 0
        values.clear()
        for value in modelInput['deviations'][chunk_start:chunk_end]:
            # Insert our current value in the circular buffer
            values.append(value)
            # If we don't have enough values skip this iteration
            if len(values) != values.maxlen:
                result.append(0)
                continue
            # Lets check if there is a sequential count
            if same_sign(values):
                sequential_finds += 1
                result.append(sequential_finds)
                if mode == 0:
                    pass
                elif mode == 1:
                    values.clear()
                elif mode == 2:
                    values.clear()
                    values.append(value)
            else:
                result.append(0)
        # Update the chunk start position for the next iteration
        chunk_start = chunk_end

    for i, j, k in zip(result, modelInput['deviations'], modelInput['results']):
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

    # SusSum = sum(sustained)
    # print(sustained)
    # print(sustained1)
    # print(SusSum)
    # print("counter: ",result)
    # modelInput['modelData']['counter'] = pd.Series(result)
    # modelInput['modelData']['sustain dev'] = pd.Series(sustained)
    #
    # modelInput['modelData'].to_excel("sustained dev 2020.xlsx")

    SustainDevOutput = {
        'sustained': sustained, 'result':result
    }
    return SustainDevOutput


