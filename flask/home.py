from flask import Flask
app = Flask(__name__)

@app.route('/home/<name>')
def hello_world(name):
   return f'Hello  {name}' 

if __name__ == '__main__':
   app.debug = True
   app.run()