from app.extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

#USER TABLE (handles auth for Vendors and Admins)
class User(db.Model):
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False) # Important for M-Pesa if vendor receives money
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False) # 'vendor' or 'admin'

    # Relationship: A User (Vendor) has one active location status
    location = db.relationship('VendorLocation', backref='vendor', uselist=False)


# 2. VENDOR LOCATION (The "Check-In" Data)
class VendorLocation(db.Model):
    __tablename__ = 'vendor_locations'
    
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Where are they?
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    # What do they have? (Matches your JSON requirement)
    # Example data: {"items": ["Samosa", "Smokie"], "prices": {"Samosa": 20}}
    menu_items = db.Column(JSON, nullable=False)

    # When did they check in? (Used for the 3-hour timer)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

# 3. TRANSACTION (For the M-Pesa Logs)
class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Link to the Vendor getting paid
    vendor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Customer info (We don't need a full Customer table, just their phone for the record)
    customer_phone = db.Column(db.String(15), nullable=False)
    
    amount = db.Column(db.Float, nullable=False)
    mpesa_receipt_number = db.Column(db.String(20), unique=True, nullable=True)
    status = db.Column(db.String(20), default='PENDING') # PENDING, COMPLETED, FAILED
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)