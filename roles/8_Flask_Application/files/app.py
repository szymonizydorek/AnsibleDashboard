from flask import Flask

print ("Executing Flask app...")

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask running inside Docker"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
