from flask import Blueprint, jsonify, request

# Define the Blueprint
bp = Blueprint('customer', __name__, url_prefix='/api/customer')

@bp.route('/search', methods=['GET'])
def search_vendors():
    # Placeholder for Member 2's Haversine Logic
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return jsonify({"message": "Search Endpoint Ready", "lat": lat, "lon": lon})