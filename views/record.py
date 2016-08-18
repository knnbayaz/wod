from flask import Blueprint, render_template
from forms import WorkoutItem

record = Blueprint('record', __name__)

@record.route('/', methods=['GET', 'POST'])
def entry():
    workoutForm = WorkoutItem()
    workoutForm.process()
    #if form.name.data != None:
    #    print(form.name.data)
    #    print(form.group.data)
    return render_template('record/entry.html', form = workoutForm)
    


