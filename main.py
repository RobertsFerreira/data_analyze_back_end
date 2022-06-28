from flask import Flask
from modules.configuration.models.config import Configuration

app = Flask('__main__')


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