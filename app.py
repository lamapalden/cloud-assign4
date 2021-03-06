from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    print ("Converting celcius to fahrenheit", flush=True)
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit) + " degree Fahrenheit"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
