from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        tweet = request.form["tweet"]
        prediction = classifier(tweet)[0]

        result = {
            "text": tweet,
            "label": prediction["label"],
            "score": round(prediction["score"] * 100, 2)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)