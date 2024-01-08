from flask import Flask,render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = "asd123"

class WebForm(FlaskForm):
    url = StringField("input the url",validators=[InputRequired()])
    submit = SubmitField("Submit")

@app.route('/',methods=['GET',"POST"])
def index():
    form=WebForm()
    flag=False
    if("done" in session):
        print("hh")
        flag=True
    if form.validate_on_submit():
        # print("hh")
        # 处理表单提交
        input_value = form.url.data
        session['url']=form.url.data
        session['done']=True
        flash(input_value)
        return redirect(url_for('index'))
    
    return render_template("form.html",form=form,done=flag)



if __name__ == '__main__':
    app.run(debug=True)