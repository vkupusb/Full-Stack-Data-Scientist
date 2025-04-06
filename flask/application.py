from flask import Flask, redirect, url_for,render_template,request

application = Flask(__name__)
app = application


@app.route('/')
def welcome():
   return "Welcome to my youtub channel"

@app.route('/home')
def welcome_home():
   return "Welomce youtube channel, please subscribe !!!"

#@app.route('/home/<string:name>')
@app.route('/home/<name>')
def home(name):
   return f'Hello  {name}'

@app.route('/results/<int:marks>')
def results(marks):
   if marks < 50:
      result = 'fail'
   else:
      result = 'success'

   return redirect(url_for(result,score=marks))


@app.route('/success/<int:score>')
def success(score):
   return render_template('results.html',result="Pass")

@app.route('/fail/<int:score>')
def fail(score):
   return render_template('results.html',result="Fail")

##result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit_marks():
   total_mark = 0
   if request.method == 'POST':
      science = int(request.form['science'])
      maths = int(request.form['maths'])
      cplusplus = int(request.form['cplusplus'])
      datascience = int(request.form['datascience'])
   total_mark = science + maths + cplusplus + datascience

   #return redirect(url_for('results',marks=total_mark))
   return render_template("results.html",result=total_mark)

@app.route('/marks')
def marks():
   return render_template('marks.html')

@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/cal',methods=["GET"])
def math_operator():
   operation = request.json["operation"]
   number1 = int(request.json["number1"])
   number2 = int(request.json["number2"])

   if operation == "add":
      result = number1 + number2
   elif operation == "sub":
      result = number1 - number2
   elif operation == "div":
      result = number1 / number2
   elif operation == "mul":
      result = number1 * number2

   return "the operation is {} and the result is {}".format(operation,result)



if __name__ == '__main__':
   app.debug = True
   app.run()