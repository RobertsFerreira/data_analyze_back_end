HOST = 'localhost'
PORT = '5000'

import json
from typing_extensions import Self

from helpers.help_file.help_file import HelpFile

PATHFILE = 'assets/configuration/configuration.json'

class Configuration():
    def __init__(self, host = 'localhost', port = '5000'):
        self.host = host
        self.port = port

    def configurationDefault() -> Self:
        return Configuration(host='localhost', port='5000')

    def readFile() -> Self | Exception:
        try:
            if not HelpFile.existFile(PATHFILE):
                configDefault =  Configuration.configurationDefault() 
                configDefault.generateFile()
        
            file = open(PATHFILE, 'r')
            configMap = json.loads(file.read())
            config = Configuration.fromMap(configMap)
            return config        
        except Exception as e:
            raise e

    def generateFile(self) -> None | Exception:
        try:
            HelpFile.createFile(PATHFILE, 'configuration.json')

            configFile = open(PATHFILE, 'w+')

            configMap = json.dumps(self.toMap(), indent=4)

            configFile.writelines(configMap)

            configFile.close()
        except Exception as e:
            raise e

    @staticmethod
    def fromMap(configMap) -> Self:
        return Configuration(
            host='localhost' if configMap['host'] == None else configMap['host'],
            port='5000' if configMap['port'] == None else configMap['port'],
        )

    def toMap(self) -> dict[str, str] :
        return {
            'host': self.host,
            'port': self.port
        }
