import csv
import pandas as pd

import numpy as np
import statsmodels.api as sm

data = pd.read_csv('../extract.csv')
data['Price'] = data['Price'].str.replace('€', '')
data['Price'] = data['Price'].str.replace(',', ',')
data['Price'] = data['Price'].astype(int)

monolocali = data[data['Type'].str.contains('Monolocale')]
bilocali = data[data['Type'].str.contains('Bilocale')]


statistiche = pd.DataFrame(columns=['Type', 'Mean', 'Median', 'Max Price', 'Min Price', 'std dev', 'Variance'])
statistiche.loc[0] = ['Monolocali', monolocali['Price'].mean(), monolocali['Price'].median(), monolocali['Price'].max(),
                      monolocali['Price'].min(), monolocali['Price'].std(), monolocali['Price'].var()]
statistiche.loc[1] = ['Bilocali', bilocali['Price'].mean(), bilocali['Price'].median(), bilocali['Price'].max(),
                      bilocali['Price'].min(), bilocali['Price'].std(), bilocali['Price'].var()]

