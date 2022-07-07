import json


class ResponseReturnModel():
    def __init__(self, statusCode, body, message = ''):
        self.message = str(message)
        self.statusCode = statusCode
        self.body = body

    def toMap(self):
        return {
            'message': self.message,
            'statusCode': self.statusCode,
            'body': self.body
        }

    def toJson(self):
        return json.dumps(self.toMap(), indent=4)