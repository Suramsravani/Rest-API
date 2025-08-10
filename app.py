from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify({username: user})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({'error': 'Invalid or existing username'}), 400
    users[username] = data.get('data', {})
    return jsonify({'message': 'User created'}), 201

@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[username] = data.get('data', users[username])
    return jsonify({'message': 'User updated'})

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[username]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)