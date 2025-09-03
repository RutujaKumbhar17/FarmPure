from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__, template_folder='.')

# Define the path to the folders where your static files are located.
# This path is relative to the location of this app.py file.
STATIC_DIR = os.path.abspath(os.path.dirname(__file__))

# ==============================================================================
# --- General Routes for HTML Pages ---
# These routes correspond to each HTML file in the project.
# The `render_template` function looks for files in the 'templates' folder by default.
# Since all HTML files are in the root directory, we specify the directory directly.
# ==============================================================================

@app.route('/')
def home():
    """Renders the main landing page (index.html)."""
    return render_template('index.html')

@app.route('/login_signup.html')
def login_signup():
    """Renders the login/signup role selection page."""
    return render_template('login_signup.html')

@app.route('/user_login.html')
def user_login():
    """Renders the user login page."""
    return render_template('user_login.html')

@app.route('/user_signup.html')
def user_signup():
    """Renders the user signup page."""
    return render_template('user_signup.html')

@app.route('/farmer_login.html')
def farmer_login():
    """Renders the farmer login page."""
    return render_template('farmer_login.html')

@app.route('/farmer_signup.html')
def farmer_signup():
    """Renders the farmer signup page."""
    return render_template('farmer_signup.html')

@app.route('/u_homepage.html')
def u_homepage():
    """Renders the user homepage."""
    return render_template('u_homepage.html')

@app.route('/f_homepage.html')
def f_homepage():
    """Renders the farmer homepage."""
    return render_template('f_homepage.html')

@app.route('/home.html')
def main_home():
    """Renders the secondary home page (same as u_homepage.html)."""
    return render_template('home.html')

@app.route('/gps.html')
def gps_page():
    """Renders the GPS page that uses the JavaScript file."""
    return render_template('gps.html')


# ==============================================================================
# --- Static File Routes ---
# These routes are necessary to serve the CSS, JS, and image files.
# The browser will request these files based on the paths in your HTML.
# ==============================================================================

@app.route('/style.css')
def serve_css():
    """Serves the main stylesheet."""
    return send_from_directory(STATIC_DIR, 'style.css')

@app.route('/your_script.js')
def serve_js():
    """Serves the main JavaScript file."""
    return send_from_directory(STATIC_DIR, 'your_script.js')

@app.route('/image/<path:filename>')
def serve_image(filename):
    """Serves image files from the 'image' subfolder."""
    return send_from_directory(os.path.join(STATIC_DIR, 'image'), filename)

# You can add more routes for other pages mentioned in the navigation,
# such as '/features.html', '/products.html', etc., as you create them.

if __name__ == '__main__':
    # Run the application in debug mode.
    # The debug=True flag automatically reloads the server on code changes.
    app.run(debug=True)
