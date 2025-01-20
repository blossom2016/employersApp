from flask import Flask, jsonify, request
from flask_cors import CORS
from dataclasses import dataclass

# Define the User dataclass
@dataclass
class User:
    id: int
    name: str
    email: str
    bio: str

# Initialize the mock database
users_db = {}
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/api/user/<int:user_id>', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the User API. Use /user/<user_id> to fetch user data."})

def create_user(id, name, email, bio):
    if id in users_db:
        raise ValueError(f"User with ID {id} already exists.")
    user = User(id, name, email, bio)
    users_db[id] = user

def seed_mock_db():
    """
    Seeds the mock database with initial users.
    """
    create_user(0, "Alice Smith", "alice@example.com", "Software Developer from NY.")
    create_user(1, "Bob Johnson", "bob@example.com", "Graphic Designer from CA.")
    create_user(2, "Charlie Lee", "charlie@example.com", "Data Scientist from TX.")

# Seed the database
seed_mock_db()

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email, "bio": user.bio}), 200
    return jsonify({"error": "User not found"}), 404
@app.route('/user', methods=['POST'])
def add_user():
    """
    Adds a new user to the database.
    Expects a JSON payload with 'id', 'name', 'email', and 'bio'.
    """
    try:
        data = request.get_json()

        # Validate input
        if not all(key in data for key in ("id", "name", "email", "bio")):
            return jsonify({"error": "Missing fields in request body. Required: id, name, email, bio."}), 400

        # Extract and add the user
        user_id = data["id"]
        name = data["name"]
        email = data["email"]
        bio = data["bio"]

        create_user(user_id, name, email, bio)
        return jsonify({"message": "User added successfully.", "user": data}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while adding the user."}), 500

if __name__ == '__main__':
    app.run(debug=True)
