import numpy as np
import pandas as pd

def removeSemDados(respostas):
    return list(filter(lambda x: x != 'Sem dados', respostas))
    


def main():
    df = pd.read_csv('data/data_pesquisa.csv', delimiter=';')
    df.replace(np.nan, 'Sem dados', inplace=True)
    print(df)

    listAllresp = []

    for index, row in df.iterrows():
        listResps = row.values.tolist()
        listResps = removeSemDados(listResps)
        # print(listResps)
        listAllresp.append(listResps)

    print(listAllresp.__len__())
    print(listAllresp[0])
main()
