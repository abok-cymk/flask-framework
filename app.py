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
        
        errors = []
        
        if not username or not username.isalpha():
            errors.append("username must only contain letters!")
            
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            errors.append("Invalid email format")
            
        if len(password) < 8:
            errors.append("❌ Password must be at least 8 characters")
        if not re.search(r'[A-Z]', password):
            errors.append("❌ Missing uppercase letter")
        if not re.search(r'[a-z]', password):
            errors.append("❌ Missing lowercase letter")
        if not re.search(r'\d', password):
            errors.append("❌ Missing number")
        
        
        if errors:
            return render_template('register.html', errors=errors)
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        users[username] = {
            'email': email,
            'password': hashed_password,
        }
        
        flash('✅ Registration successful!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
            
    