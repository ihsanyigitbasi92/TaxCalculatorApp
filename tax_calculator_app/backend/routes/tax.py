from flask import Blueprint, request, jsonify
from models.tax_record import TaxRecord
from utils.calculations import calculate_tax

bp = Blueprint('tax', __name__, url_prefix='/tax')

@bp.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    income = data.get('income')
    deductions = data.get('deductions')
    state = data.get('state')
    filing_status = data.get('filing_status')
    tax_due = calculate_tax(income, deductions, state, filing_status)
    return jsonify({'tax_due': tax_due}), 200