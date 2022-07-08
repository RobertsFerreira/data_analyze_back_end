from flask import Flask, request, flash
from werkzeug.exceptions import *
from models.error.generic_error import FileSelectError
from module.configuration.models.config import Configuration
from models.response_return.response_return_model import ResponseReturnModel
from module.files.file_store import FileStore

app = Flask('__main__')

@app.route('/upload', methods=['POST'])
def upload_file():
    try :
        file = request.files['file']
        fileStore = FileStore()
        file = fileStore.formatDateFile(file)
        responseReturn = ResponseReturnModel(message=f'Nome do arquivo: {file}', statusCode=200, body={'file': file})
        jsonResponse = responseReturn.toJson()
        return jsonResponse
    except BadRequestKeyError as e:
        responseReturn = ResponseReturnModel(message=e, statusCode=e.code, body={})
        jsonResponse = responseReturn.toJson()
        return jsonResponse, e.code
    except FileSelectError as error:
        responseReturn = ResponseReturnModel(message=e, statusCode=500, body=error.toMap())
        jsonResponse = responseReturn.toJson()
        return jsonResponse, responseReturn.statusCode
    except Exception as e:
        responseReturn = ResponseReturnModel(message=e, statusCode=500, body={})
        jsonResponse = responseReturn.toJson()
        return jsonResponse, responseReturn.statusCode

@app.route('/sobre', methods=['GET'])
def sobre():
    return {
            'version': '0.0.1',
           } 

def initServer():
    config = Configuration.readFile()
    from waitress import serve
    serve(app, host=config.host, port=config.port)

def main():
   if __name__ == '__main__':
    initServer()

main()