from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "ibiubiniuiyvciwgeug" # Required for session management

#Sample user data (this would normally come from a database)
user_data = {
  'name': 'John Doe',
  'email': 'john.doe@example.com'
}

@app.route('/profile')
def profile():
  # Render the profile page with user data
  return render_template('user_dashboard.html', user=user)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Get updated profile data from the form
    name = request.form.get('name')
    email = request.form.get('email')

    # Simulate updating user data (you'd normally update a database)
    user_data['name'] = name
    user_data['email'] = email

    return jsonify({'success': True})  # Respond with success status

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
        return render_template('user_dashboard.html', user=user_data)
    return redirect(url_for('home'))

# Analyst dashboard route
@app.route('/analyst_dashboard')
def analyst_dashboard():
    if 'role' in session and session['role'] == 'analyst':
        return render_template('analyst_dashboard.html')
    return redirect(url_for('home'))

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    # You would run your drought prediction model here
    # For now, we'll return dummy data for the chart

    prediction_data = [20, 30, 45, 60, 50, 40, 30]  # Dummy data
    return jsonify({'prediction': prediction_data})

# Logout route
@app.route('/logout')
def logout():
  session.pop('role', None)
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
