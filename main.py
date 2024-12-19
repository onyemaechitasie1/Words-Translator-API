from flask import Flask, render_template
import pandas as pd

df = pd.read_csv("dictionary.csv")
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    word_meaning = df.loc[df['word'] == word]['definition'].squeeze()
    return {"definition": word_meaning,
            "word": word}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
