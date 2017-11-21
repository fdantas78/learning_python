from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        x =1
        x = 1 +y
        return "Hello World again"
    except Exception as e:
        return(str(e))
        

if __name__ == "__main__":
    app.run()

