import traceback
import numpy as np
import pandas as pd
from models.error.generic_error import FileSelectError
from io import StringIO

class FileStore():

    def load(self, file):
        try:
            if file.filename == '':
                raise FileSelectError('No file selected to upload')
        
            fileRead = file.stream.read().decode("utf-8")

            return fileRead
        
        except FileSelectError as e:
            raise FileSelectError(
                    message=e.message, 
                    stackTrace=traceback.format_exc(), 
                    typeError=e.__class__
                )

    def formatDateFile(self, file):
        fileRead = self.load(file)
        fileIo = StringIO(fileRead)
        df = pd.read_csv(fileIo, delimiter=';')
        df.replace(np.nan, 'Sem dados', inplace=True)
        df.replace('0', 'Sem dados', inplace=True)
        print(df)
        return file.filename