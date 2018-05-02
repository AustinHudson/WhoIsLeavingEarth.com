
from flask import Flask, render_template
from spaceTracker import simple_get, getDateInfo, getLaunchInfo
app = Flask(__name__)


@app.route("/home")
def home():

    return render_template("landingPage.html")


@app.route("/output")
def output():

    return render_template("index.html", dateList=getDateInfo())


if __name__ == "__main__":
    app.run()