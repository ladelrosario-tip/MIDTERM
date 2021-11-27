from flask import Flask, json, render_template

midterm = Flask('midterm_app')

@midterm.route("/")

def login():
    return render_template('login.html')

@midterm.route("/register")

def register():
    return render_template('registration.html')

if __name__ == '__main__':
    midterm.run(host='0.0.0.0', port=5000)