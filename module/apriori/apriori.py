from helpers.utils.utils import removeSemDados
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

from module.apriori.models.apriori_result import AprioriResult

class Apriori:
    def __init__(self, data):
        self.data = data
        self.combinations = []

    def generateCombinations(self):
        for _, row in self.data.iterrows():
            combination = row.values.tolist()
            combination = removeSemDados(combination)
            self.combinations.append(combination)

    def generatedTransaction(self):
        transaction = TransactionEncoder()
        _transactions = transaction.fit(self.combinations).transform(self.combinations)
        transactions = pd.DataFrame(_transactions, columns=transaction.columns_)
        return transactions

    def executeApriori(self, transactions):
        frequency = apriori(transactions, min_support=0.01, use_colnames=True)
        frequency.sort_values(by=['support'], ascending=False)

        rules = association_rules(frequency, min_threshold=0.2)
        rules = rules.sort_values(by=['lift'], ascending=False).drop(['antecedent support',  'consequent support',   'support', 'leverage',  'conviction'], axis=1)

        lift = list(rules['lift'])
        consequents = rules['consequents']
        antecedents = rules['antecedents']
        results = []

        for index, item in enumerate(lift):
            consequent = list(consequents[index])[0]
            antecedent = list(antecedents[index])[0]
            aprioriResult = AprioriResult(
                lift=item,
                consequent=consequent,
                antecedent=antecedent
            )

            aprioriMap = aprioriResult.toMap()
            results.append(aprioriMap)

        return results

