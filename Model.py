import wtforms as wtf
from wtforms import Form, FloatField, validators, StringField


class InputForm(Form):
    expressionInX = StringField('note', validators=[validators.InputRequired()])
    domain = StringField('note', validators=[validators.InputRequired()])
    eCurves = wtf.SelectField(label='', choices=[('yes', 'Yes'),
      ('no', 'No')])

