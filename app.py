from flask import Flask

# Creates an application
app = Flask(__name__)


@app.route('/')
def inde():
    return "Hello World"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # host
    # port
    # debugput