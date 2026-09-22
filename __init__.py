from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)

# Enable CORS
CORS(app)

# Configure security headers using Talisman
Talisman(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
