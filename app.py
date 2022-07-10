from flask import Flask

app=Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
    return "Hello, This is Jagadeesh.K world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)