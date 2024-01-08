from reptile import reptile

import torch.nn as nn
from model.config import network


class MPLNetWork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.network = network

    def forward(self, x):
        # x = self.flatten(x)
        logits = self.network(x)
        return logits


from model import model
from flask import Flask,render_template,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = "asd123"
from test import check_url

class WebForm(FlaskForm):
    url = StringField("input the url",validators=[InputRequired()])
    submit = SubmitField("Submit")

@app.route('/',methods=['GET',"POST"])
def index():
    form=WebForm()
    flag=False
    code=2
    answer=""

    if ("done" in session):
        print("hh")
        flag = True
        response = check_url(session['url'])
        code = response[0]
        answer = response[1]
        session.clear()
    if form.validate_on_submit():
        input_value = form.url.data
        session['url']=form.url.data
        session['done']=True
        flash(input_value)
        return redirect(url_for('index'))

    return render_template("form.html",form=form,done=flag,code=code,answer=answer)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)