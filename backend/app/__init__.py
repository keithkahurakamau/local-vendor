from flask import Flask
from app.extensions import db, cors
from config import DevelopmentConfig
import os
from dotenv import load_dotenv

load_dotenv()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    
    # 1. Load the Configuration
    app.config.from_object(config_class)

    # 2. Safe Debug Print (Won't crash)
    # This will print "None" if the key is missing, instead of killing the app
    print(f"🔍 DEBUG: Database URL is -> {app.config.get('SQLALCHEMY_DATABASE_URI')}")

    # 3. Initialize Extensions
    db.init_app(app)
    cors.init_app(app)

    # 4. Register Blueprints
    from app.routes import customer
    app.register_blueprint(customer.bp)

    # 5. CLI Command
    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("✅ Database tables created successfully!")

    return app