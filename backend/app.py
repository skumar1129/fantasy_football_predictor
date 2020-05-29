from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_graphql import GraphQLView


app=Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MONGO_DBNAME'] = 'Fantasy_Football'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Fantasy_Football'

mongo = PyMongo(app)


@app.route('/player/<playername>')
def find_player(playername):
    player_score = mongo.db.PlayersScore
    player = player_score.find_one({"name": playername})
    if player:
        return jsonify({
            'name': player['name'],
            'fantasyScores': player['fantasyScores'],
            'pprScore': player['pprScore'],
            'draftKingScore': player['draftKingScore'],
            'fanDuelScore': player['fanDuelScore']
        })
    else:
       return jsonify({'results': 'None Found'})
        

@app.route('/')
def hello_world():
    return 'Hello World'