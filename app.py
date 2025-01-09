from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"]="138.41.20.102"
app.config["MYSQL_PORT"]= 53306
app.config["MYSQL_DB"]= "w3schools"
app.config["MYSQL_USER"]="ospite"
app.config["MYSQL_PASSWORD"]="ospite"

mysql = MySQL(app)
@app.route("/")
def home():
    return render_template("Homepage.html", titolo="HomePage")

@app.route('/products')
def products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    return render_template('Products.html', title="Prodotti", products=products)

@app.route('/category')
def category():
    return render_template("Category.html")




  