from flask import Flask
app = Flask(__name__)

@app.route("/" )
def home():
  return """
  <h1> Campus Lost & Found</h1>
  <p>Welcome to our Campus
item recovery system!</p>
 """

if __name__ == "__main__":
  app.ren(debug=True)
