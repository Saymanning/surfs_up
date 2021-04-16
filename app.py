# 1 Import Flask
from flask import Flask

# 2 Create an app
app = Flask(__name__)

# 3 Define index route
@app.route('/')
def home():
    print("Server received request from 'About' page...")
    return ("Welcome to my 'About' page...")


# 4 Define the about route
    @app.route("/about")
    def about():
        print("Server received request from 'About' page...")
        return ("Welcome to my 'About' page...")

# Define contact route
@app.route("/contact")
def contact():
    print("Server received request from 'Contact' page...")
    return ("Welcome to my 'Contact' page...")

# 6 Define main behavior
if __name__=="__main__":
    app.run(debug=True)

