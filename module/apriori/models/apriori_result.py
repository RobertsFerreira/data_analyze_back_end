import json

class AprioriResult():
    def __init__(self, lift, consequent, antecedent):
        self.lift = lift
        self.consequent = consequent
        self.antecedent = antecedent

    def toMap(self):
        return {
            "lift": self.lift, 
            "consequent": self.consequent,
            "antecedent": self.antecedent,
        }

    def toJson(self):
       return json.dumps(self.toMap())