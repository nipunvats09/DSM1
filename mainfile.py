import pandas as pd
import numpy as np
from GetInputs import *
from overdrawSafe import *
from underdrawSafe import *
from sustainDeviationsSafe import sustainDeviation
from OutputEvaluation import outputEval

def mainFile():
    print("getting input values....")
    gettingInput = getInput()

    print("calculating the overdraw penatlties...")
    overdraws = overdraw(57,76,95,gettingInput)

    print("calculating the underdraw penalties and receivables...")
    underdraws = underdraw(57,gettingInput)

    print("calculating the sustain deviations penalties and counts...")
    sustainDev = sustainDeviation(gettingInput)

    print("exporting resutls into an excelfile...")
    outputEvaluation = outputEval(gettingInput, underdraws, overdraws, sustainDev)
mainFile()