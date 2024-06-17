from flask import Flask
from dateutil.easter import easter
from dateutil.easter import EASTER_WESTERN

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! Easter will next occur on '%s'" % easter(2025, EASTER_WESTERN)

if __name__ == "__main__":
    app.run()