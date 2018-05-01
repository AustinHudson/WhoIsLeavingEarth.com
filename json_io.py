
from flask import Flask, render_template
from spaceTracker import simple_get, getDateInfo, getLaunchInfo
app = Flask(__name__)

@app.route("/output")
def output():

    return render_template("index2.html", dateList=getDateInfo())

if __name__ == "__main__":
    app.run()