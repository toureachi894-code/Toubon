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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
