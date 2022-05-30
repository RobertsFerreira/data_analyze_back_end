import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('data/teste.csv', delimiter=';')
    df.replace(np.nan, 'Sem dados', inplace=True)
    print(df)

    for index, row in df.iterrows():
        listResps = row.values.tolist()
        print(listResps)
        if(index > 1):
            break

main()
