from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dictionary/<string:word>")
def dictionary(word):
    d={'apple':'사과','banana':'바나나','orange':'오렌지'}
    if word in d:
        word2 = d[word]
    else :
        word2 = "나만의 단어장에 없는 단어입니다!"
    return render_template("dictionary.html",word=word,word2=word2)
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
