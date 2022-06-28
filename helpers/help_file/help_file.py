import os

class HelpFile():

    @staticmethod
    def existFile(path) -> bool: 
        return os.path.exists(path)

    @staticmethod
    def existFolder(dir) -> bool:
        return os.path.exists(dir)      
    
    def _createFolder(dir) -> None:
        os.makedirs(dir)

    @staticmethod
    def createFile(pathFile: str, suffix: str) -> None | Exception:
        try:
            dir = pathFile.removesuffix(suffix)
            if not HelpFile.existFolder(dir):
                HelpFile._createFolder(dir)
            file = open(pathFile, 'w')
            file.close()
        except Exception as e:
            return e
