
from flask import Flask, render_template
from spaceTracker import simple_get, getDateInfo, getLaunchInfo
app = Flask(__name__)

@app.route("/output")
def output():

<<<<<<< HEAD
    return render_template("index.html", dateList=getDateInfo())
=======
    return render_template("index2.html", dateList=getDateInfo())
>>>>>>> Formatting-attempt

if __name__ == "__main__":
    app.run()