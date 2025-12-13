# local-vendor
Hyper-Local Vendor Inventory & Finder
📌 Project Overview
A real-time full-stack web application connecting customers with nearby street food vendors. Features geospatial search (5km radius), vendor "freshness" tracking, and M-Pesa integration.

🚀 Tech Stack
Frontend: React, Tailwind CSS, Leaflet Maps
Backend: Python Flask, SQLAlchemy
Database: PostgreSQL
Integration: Safaricom Daraja API (M-Pesa)
🛠️ Setup Instructions
1. Backend Setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Functionality Proof
flask --app run init-db
flask run

 ### 2. frontend setup
    cd frontend
    npm install
    npm start
