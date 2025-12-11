from flask import Flask
from app.extensions import db, cors
from config import DevelopmentConfig # Import your new config

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    
    # --- Load Config from config.py ---
    app.config.from_object(config_class)

    # --- Initialize Extensions ---
    db.init_app(app)
    cors.init_app(app)

    # --- Register Blueprints ---
    from app.routes import customer
    app.register_blueprint(customer.bp)

    # --- CLI Command: Init Database ---
    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("✅ Database tables created successfully!")

    return app