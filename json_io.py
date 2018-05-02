
from flask import Flask, render_template
from spaceTracker import simple_get, getDateInfo, getLaunchInfo
app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/missions")
def output():

    return render_template("missions.html", dateList=getDateInfo())


if __name__ == "__main__":
    app.run()