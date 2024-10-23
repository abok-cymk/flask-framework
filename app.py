from flask import Flask, render_template, request, redirect, url_for, flash
import re
import bcrypt
import mysql.connector

DATABASE_HOST="localhost"
DATABASE_USER="root"
DATABASE_PASSWORD="m1a2i3L4$"
DATABASE_NAME="user_db"

app = Flask(__name__)
app.secret_key = 'ahahxsdhwugdyedgyediiehudie'

def database_config():
    try:
        conn = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
        return conn
    except mysql.connector.Error as err:
        flash(f"Error: Unable to connect to the database {err}")
        return None
        
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    conn = database_config()
    
    if conn is None:
        flash("Error: Unable to connect to the database", "danger")
        return render_template('register.html')
    
    
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
            
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            values = (username, email, hashed_password)
            cursor.execute(sql, values)
            conn.commit()
            
            flash('✅ Registration successful!', 'success')
            return redirect(url_for('home'))
        except mysql.connector.Error as err:
            flash(f"Unable to connect to the database {err}", "danger")
            return render_template('register.html')
        finally:
            if conn:
                cursor.close()
                conn.close()
            
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
            
    