from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask on AWS Lambda!'

if __name__ == "__main__":
    app.run()
