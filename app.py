import subprocess
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/commande", methods=["POST"])
def commande():
    data = request.get_json()
    donner = data.get("donner")

    commande = donner.split()
    result = subprocess.run(
            commande,
            text=True,
            capture_output=True
                    )
    return {
        "message": result.stdout
            }


app.run(
     port=3000,
     host="0.0.0.0",
     debug=True
)
