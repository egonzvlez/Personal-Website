from flask import Flask

# Creates an application
app = Flask(__name__)


@app.route('/')
def home():
    return "Home Page"

@app.route('/AboutMe')
def about():
    return "About Me "

@app.route('/Projects')
def projects():
    return "Projects"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # host
    # port
    # debugput