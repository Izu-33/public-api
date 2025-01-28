from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    data = {
        "email": "dizundu@yahoo.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "github_url"
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)