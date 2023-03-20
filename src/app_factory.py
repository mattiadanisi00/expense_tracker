from flask import Flask
import database


def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')

    # register the database
    with app.app_context():
        database.init_db()

    return app
