from flask import Flask
from BluePrint.accidents import accidents_blueprint

app = Flask(__name__)

app.register_blueprint(accidents_blueprint)

if __name__ == '__main__':
    app.run(debug=True)