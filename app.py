from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def presentation():
    return render_template('index.html')

if __name__ == '__main__':
    # Runs on http://localhost:5000
    app.run(debug=True, port=5000)