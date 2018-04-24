from flask import Flask, render_template
from spaceTracker import simple_get, getWebInfo
app = Flask(__name__)

@app.route("/output")
def output():


    return render_template("index.html", missionList=getWebInfo())

if __name__ == "__main__":
    app.run()