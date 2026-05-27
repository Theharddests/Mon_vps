from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Mon mini VPS fonctionne"
port = int(os.environ.get("PORT", 10000))

app.run(host="0.0.0.0", port=8080)
