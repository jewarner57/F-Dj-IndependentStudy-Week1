from flask import Flask, Blueprint
from config import Config
from main.routes import main
from party.routes import party

app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(main)
app.register_blueprint(party)


if __name__ == '__main__':
    app.run(debug=True)
