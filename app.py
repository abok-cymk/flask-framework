from flask import Flask, render_template, request, redirect, url_for, flash
import re
import bcrypt

app = Flask(__name__)
app.secret_key = 'ahahxsdhwugdyedgyediiehudie'

users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        
        if not username or not username.isalpha():
            flash("username must only contain letters!")
            return redirect(url_for('register'))
    