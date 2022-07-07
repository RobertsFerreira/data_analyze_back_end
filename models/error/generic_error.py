import json


class GenericError(Exception):
    def __init__(self, message, stackTrace = ''):
        self.message = message
        self.stackTrace = stackTrace
        super().__init__(self.message)

class FileSelectError(Exception):
    def __init__(self, message='', typeError = None, stackTrace = ''):  
        self.message = message
        self.stackTrace = stackTrace
        self.typeError = typeError
        super().__init__(self.message)
    
    def toMap(self):
        return {
            'typeError': str(self.typeError),
            'stacktrace': self.stackTrace,
        }
