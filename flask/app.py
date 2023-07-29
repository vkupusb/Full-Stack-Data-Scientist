from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/home/<name>')
def home_1(name):
   return f'Hello  {name}'


@app.route('/index')
def index():
   return render_template('index')


if __name__ == '__main__':
   app.debug = True
   app.run()