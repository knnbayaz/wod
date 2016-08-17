from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class WorkoutItem(Form):
    groupChoices = [('bar', 'Barbell'), ('car', 'Cardio')]
    name = StringField('name', validators=[DataRequired()])
    group = SelectField('group', choices = groupChoices, default = 1)