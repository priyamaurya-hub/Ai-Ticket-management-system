from flask import Flask
from routes import ticket

app = Flask(__name__)

app.register_blueprint(ticket)

@app.route("/")
def home():
    return "AI Ticket Management Backend Running"

if __name__ == "__main__":
    app.run(debug=True)