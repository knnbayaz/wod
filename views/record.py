from flask import Blueprint, render_template
from forms import WorkoutItem
import os


record = Blueprint('record', __name__, template_folder='/home/ubuntu/workspace/ex50/templates/record')

@record.route('/', methods=['GET', 'POST'])
def entry():
    workoutForm = WorkoutItem()
    workoutForm.process()
    #if form.name.data != None:
    #    print(form.name.data)
    #    print(form.group.data)
    return render_template('entry.html', form = workoutForm)
    


