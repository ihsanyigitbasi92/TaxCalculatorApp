from flask import Blueprint, request, jsonify
from models.user import User

bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/update', methods=['POST'])
def update_profile():
    data = request.get_json()
    # Add profile update logic here
    return jsonify({'message': 'Profile updated successfully'}), 200