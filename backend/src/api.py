import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()

## ROUTES

@app.route('/drinks', methods=['GET'])
def get_drinks():
'''
    This function handles requesting all available drinks in a short form
    Permission: Public
'''
    drinks = Drink.query.all()

    formatted_drinks = [drink.short() for drink in drinks]

    return jsonify({
        'success': True,
        'drinks': formatted_drinks
    })


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_detailed_drinks(payload):
'''
    This function handles requesting all available drinks with all information 
    Permission: get:drinks-detail
'''
    drinks = Drink.query.all()

    formatted_drinks = [drink.long() for drink in drinks]
    # if drinks:
    #     formatted_drinks = [drink.long() for drink in drinks]
    # else:
    #     formatted_drinks = drinks
    return jsonify({
        'success': True,
        'drinks': formatted_drinks
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(payload):
'''
    This function handles inserting a new drink. 
    Permission: post:drinks
'''
    data = request.get_json()
    is_data_valid = (data is not None) and ('title' in data) and ('recipe' in data)
    if not is_data_valid:
        abort(400)

    is_drink_duplicate = Drink.query.filter(Drink.title == data['title']).first()
    if is_drink_duplicate:
        abort(422)

    drink = Drink(title=data['title'], recipe=json.dumps(data['recipe']))
    drink.insert()
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
'''
    This function handles updating an existing drink. 
    Permission: post:drinks
'''
    drink = Drink.query.get_or_404(drink_id)
    data = request.get_json()
    is_data_valid = (data is not None) and (('title' in data) or ('recipe' in data))
    if not is_data_valid:
        abort(400)
    if 'title' in data:
        drink.title = data['title']
    if 'recipe' in data:
        drink.recipe = data['recipe']
    drink.update()

    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
'''
    This function handles deleting an existing drink. 
    Permission: post:drinks
'''
    drink = Drink.query.get_or_404(drink_id)
    drink.delete()

    return jsonify({
        'success': True,
        'delete': drink_id
    })
## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
