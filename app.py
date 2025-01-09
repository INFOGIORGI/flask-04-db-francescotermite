from flask import Flask

app = Flask(__name__)

lista=(("Capocollo", "SC1", 2), ("Marmellata", "SC2", 3), ("Caffè", "SC3", 1.50))

@app.route("/")
def homepage():
    return render_template("Homepage.html")

@app.route("/Product")
app.run(debug=True)
