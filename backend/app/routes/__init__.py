from flask import Flask
from app.extensions import db, cors
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # --- Week 1 Config: Database Only ---
    # Source: Capstone Guide [cite: 97, 120]
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Initialize Extensions ---
    db.init_app(app)
    cors.init_app(app)

    # --- Register Blueprints ---
    # Week 1 Requirement: "Basic Read (GET) routes" 
    from app.routes import customer
    app.register_blueprint(customer.bp)

    # --- CLI Command ---
    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("✅ Database tables created successfully!")

    return app