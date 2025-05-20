
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="mysql",
    user="appuser",
    password="appuserpass",
    database="testdb"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    if name:
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
