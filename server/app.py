from flask import Flask, jsonify
from .config import Config
from . import db, migrate
from .models import *
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to the Pizza Restaurant API!',
            'endpoints': [
                '/restaurants',
                '/pizzas',
                '/restaurant_pizzas'
            ]
        })

    return app
