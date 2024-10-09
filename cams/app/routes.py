from flask import Blueprint, jsonify, request
from . import db
from .models import Test

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
def test():
    return "test"

@api_bp.route('/dbtest', methods=['POST'])
def add_test():
    data = request.get_json()
    testfield = data.get('testfield')

    if not testfield:
        return jsonify({'error': 'Invalid input'}), 400

    # Create a new test object
    new_test = Test(testfield=testfield)
    
    # Add to the database
    db.session.add(new_test)
    db.session.commit()

    return jsonify({'message': 'Test added successfully!', 'test': new_test.serialize()}), 201

# GET: Fetch all tests from the database
@api_bp.route('/dbtest', methods=['GET'])
def get_tests():
    tests = Test.query.all()
    return jsonify([test.serialize() for test in tests]), 200