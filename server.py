from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/', methods=['GET'])

def hello():
    data = {"slackUsername":"Triumph Edet", "backend":True, "age":17, "bio":"An aspiring backend engineer ready to face the world of tech"}
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
