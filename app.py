from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import sys
import os

app = Flask(__name__)
api = Api(app)

persons = [
    {"id": 1, "name": "Jane", "age": 25,
        "gender": "Female", "email": "jane@example.com"},
    {"id": 2, "name": "Levi", "age": 33,
        "gender": "Male", "email": "levi@example.com"}
]

# Retrieve a list of all person objects.


@app.route('/persons', methods=['GET'])
def get_persons():
    return jsonify(persons)

# Create a new person object.


@app.route('/persons', methods=['POST'])
def create_person():
    person = {
        'id': len(persons) + 1,
        'name': request.json['name'],
        'age': request.json['age'],
        'gender': request.json['gender'],
        'email': request.json['email']
    }
    persons.append(person)
    return jsonify(person), 201


# Retrieve a specific person object by its ID.

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    for person in persons:
        if person["id"] == person_id:
            return jsonify(person)
    return jsonify({"error": "Person not found"}), 404

# Update a specific person object by its ID.


@app.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    for person in persons:
        if person["id"] == person_id:
            person.update(request.json)
            return jsonify(person)
    return jsonify({"error": "Person not found"}), 404



# Delete a specific person object by its ID.


@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    for person in persons:
        if person["id"] == person_id:
            persons.remove(person)
            return "", 204
    return jsonify({"error": "Person not found"}), 404


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
