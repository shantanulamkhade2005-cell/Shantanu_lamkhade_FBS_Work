from flask import Flask,render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verify')
def verify():
    return 'iam in verify page'

@app.route('/register')
def register():
    return "Register Page"
if __name__ == '__main__':
    app.run()