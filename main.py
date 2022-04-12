from dotenv import load_dotenv
from flask import Flask
load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)

