import pandas as pd
from unidecode import unidecode
import re

file_path_input = r'D:\Roit\TestingPython\inputData.xlsx'
file_path_output = r'D:\Roit\TestingPython\outputData.xlsx'

# remove accents and transform the text to lower case
def remove_accents_and_lowercase(text):
    return unidecode(str(text)).lower()

# regex to substitute any non numeric value with an empty string
def remove_non_numeric(text):
    return re.sub(r'\D', '', str(text))

# create a data frame with pandas
df = pd.read_excel(file_path_input)

def format_excel():
    # create a copy of the dataframe and map the even columns and the odd columns with the respective functions
    df.iloc[:, 1::2] = df.iloc[:, 1::2].applymap(remove_accents_and_lowercase)
    df.iloc[:, 2::2] = df.iloc[:, 2::2].applymap(remove_non_numeric)

    df.to_excel(file_path_output, index=False)
