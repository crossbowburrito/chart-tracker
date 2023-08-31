from flask_cors import CORS
from flask import Flask, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

app = Flask(__name__)
CORS(app)

MONGODB_URI = os.environ['MONGODB_URI']

@app.route('/songs', methods=['GET'])
def get_songs():
    client = MongoClient(MONGODB_URI)
    db = client['chart-tracker']
    collection = db['songs']
    songs = list(collection.find({}, {'_id': 0}))
    return jsonify(songs)


@app.route('/', methods=['GET'])
def chorusgen():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
