from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    if request.args.get("name"):
        name = request.args.get("name")
    else:
        name = " Bob"
    return "<marquee>Hello!" + name + "</marquee>"


@app.route("/bye")
def bye():
    return "<marquee>Bai</marquee>"


if __name__ == "__main__":
    app.run()