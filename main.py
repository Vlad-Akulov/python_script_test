import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!doctype html>
    <html>
      <head>
        <title>Flask Test</title>
      </head>
      <body>
        <h1>Hello from Flask</h1>
        <p>This is raw HTML.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
