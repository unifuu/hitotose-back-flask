from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - you can replace this with your actual data handling logic
games = [
    {"id": 1, "title": "Red Dead Redemption 2", "genre": "Action-adventure", "platform": "PS4", "developer": "Rockstar Games"},
    {"id": 2, "title": "The Legend of Zelda: Breath of the Wild", "genre": "Action-adventure", "platform": "Switch", "developer": "Nintendo"},
]

# Endpoint to get all games
@app.route('/api/games', methods=['GET'])
def get_games():
    return jsonify(games)

# Endpoint to get a specific game by ID
@app.route('/api/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = next((game for game in games if game['id'] == game_id), None)
    if game:
        return jsonify(game)
    return jsonify({'message': 'Game not found'}), 404

# Endpoint to add a new game
@app.route('/api/games', methods=['POST'])
def add_game():
    new_game = request.json
    games.append(new_game)
    return jsonify(new_game), 201

if __name__ == '__main__':
    app.run(debug=True)