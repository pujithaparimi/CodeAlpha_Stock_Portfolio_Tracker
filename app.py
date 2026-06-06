from flask import Flask, render_template, request

app = Flask(__name__)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 170
}

@app.route("/", methods=["GET", "POST"])
def home():

    total = None

    if request.method == "POST":

        stock = request.form["stock"].upper()
        quantity = int(request.form["quantity"])

        if stock in stock_prices:
            total = stock_prices[stock] * quantity

    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)