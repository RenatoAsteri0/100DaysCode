import random
import random

import pandas as pd
def somar(num,num1):
    return num + num1

somas = (map(somar,(2,3),(1,3)))
print(list(somas))

data = pd.read_csv('data/french_words.csv')
data_dict = data.to_dict()
print(random.choice(data_dict))