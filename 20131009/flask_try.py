from flask import Flask

app = Flask(__name__)

def fb(n):
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz" 
    if not out:
        return n
    return out

@app.route("/")
def index():
    return "Hello World!"

@app.route("/<n>")
def fb_flask(n):
    return str(fb(int(n)))

if __name__ == "__main__":
    app.run(debug=True)
