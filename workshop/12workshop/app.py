from flask import Flask , render_template   
app = Flask(__name__)

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

@app.route("/12workshop")
def workshop12():
    return render_template("12workshop.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)