from flask import Flask
application = Flask(__name__)

@application.route("/hellobas")
def hello():
    return "Hello Bas!"

if __name__ == "__main__":
    application.run()
