import numpy as np
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def removeSemDados(respostas):
    return list(filter(lambda x: x != 'Sem dados', respostas))

def main():
    df = pd.read_csv('data\data_pesquisa.csv', delimiter=';')
    df.replace(np.nan, 'Sem dados', inplace=True)
    df.replace('0', 'Sem dados', inplace=True)
    print(df)
    print()

    listAllresp = []

    for _, row in df.iterrows():
        listResps = row.values.tolist()
        listResps = removeSemDados(listResps)
        # print(listResps)
        listAllresp.append(listResps)

    print('\n\n')


    te = TransactionEncoder()
    te_ary = te.fit(listAllresp).transform(listAllresp)
    df_te = pd.DataFrame(te_ary, columns=te.columns_)
    print(df_te)
    print()

    freq_item = apriori(df_te, min_support=0.01, use_colnames=True)
    freq_item.sort_values(by=['support'], ascending=False)
    print(freq_item)

    rules = association_rules(freq_item, metric="confidence", min_threshold=0.8)
    rules = rules.sort_values(by=['lift'], ascending=False).drop(['antecedent support',  'consequent support',   'support', 'leverage',  'conviction'], axis=1)
    print(rules)
main()