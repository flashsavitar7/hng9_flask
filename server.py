from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])

def hello():
    data = {"SlackUsername":"Triumph Edet", "Backend":True, "Age":17, "Bio":"An aspiring backend engineer ready to face the world of tech"}
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
