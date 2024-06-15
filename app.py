from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)  # Ajoutez cette ligne pour autoriser les requêtes cross-origin

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birth_day = db.Column(db.String(10), nullable=False)
    birth_month = db.Column(db.String(10), nullable=False)
    birth_year = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birth_day=data['birth_day'],
        birth_month=data['birth_month'],
        birth_year=data['birth_year'],
        phone_number=data['phone_number']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birth_day': user.birth_day,
        'birth_month': user.birth_month,
        'birth_year': user.birth_year,
        'phone_number': user.phone_number
    } for user in users])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
