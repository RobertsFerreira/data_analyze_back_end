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

    def executeApriori(self, transactions, minSupport = 0.01, minThreshold = 0.01):
        frequency = apriori(transactions, min_support=minSupport, use_colnames=True)
        frequency.sort_values(by=['support'], ascending=False)

        rules = association_rules(frequency, min_threshold=minThreshold)
        rules = rules.sort_values(by=['lift'], ascending=False).drop(['antecedent support',  'consequent support',   'support', 'leverage',  'conviction'], axis=1)

        lift = list(rules['lift'])
        consequents = rules['consequents']
        antecedents = rules['antecedents']
        results = []

        for index, item in enumerate(lift):
            indexRules =  list(rules.axes[0])[index]
            consequent = list(consequents[indexRules])[0]
            antecedent = list(antecedents[indexRules])[0]
            aprioriResult = AprioriResult(
                lift=item,
                consequent=consequent,
                antecedent=antecedent
            )

            aprioriMap = aprioriResult.toMap()
            results.append(aprioriMap)

        return results

