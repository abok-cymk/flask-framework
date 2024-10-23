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
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            flash("Inavlid email format")
            return redirect(url_for('register'))
        
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'
        if len(password) < 8 or not re.match(password_pattern, password):
            flash("Password must contain at least one uppercase letter, one lowercase letter, one number and be at least 8 characters!")
            return redirect(url_for('register'))
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        users[username] = {
            'email': email,
            'password': password,
        }
        
        flash('Registration successful!')
        return redirect(url_for('home'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
            
    