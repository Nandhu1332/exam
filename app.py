from flask import render_template,request,Flask
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['post'])
def submit():
    user=request.form['username']
    roll=request.form['rollno']
    email=request.form['email']
    year=request.form['year']
    return render_template('result.html',us=user,ro=roll,em=email,yr=year)
if __name__=='__main__':
    app.run(debug=True)
