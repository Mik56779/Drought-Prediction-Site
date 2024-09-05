from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "ibiubiniuiyvciwgeug" # Required for session management

#Home (Login) route
@app.route('/')
def home():
  return render_template('login.html')

#User and Analyst login route
@app.route('/login', methods=['POST'])
def login():
  username = request.form['username']
  password = request.form['password']

  #Simple user/analyst validation (to be replaced by database)
  if username == "user" and password == "userpass":
    session['role'] = 'user'
    return redirect(url_for('user_dashboard'))
  elif username == 'analyst' and password == 'analystpass':
    session['role'] = 'analyst'
    return redirect(url_for('analyst_dashboard'))
  else:
    return "invalid Credentials"

# User dashboard route
@app.route('/user_dashboard')
def user_dashboard():
    if 'role' in session and session['role'] == 'user':
        return render_template('user_dashboard.html')
    return redirect(url_for('home'))

# Analyst dashboard route
@app.route('/analyst_dashboard')
def analyst_dashboard():
    if 'role' in session and session['role'] == 'analyst':
        return render_template('analyst_dashboard.html')
    return redirect(url_for('home'))

# Logout route
@app.route('/logout')
def logout():
  session.pop('role', None)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
