from flask_sqlalchemy import SQLAlchemy
from application.app import app



db = SQLAlchemy(app)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    workoutgroup_id = db.Column(db.Integer, db.ForeignKey('workoutgroup.id'))
    
    
    def __init__(self, name, group):
        self.Name = name
        self.GroupId = group.Id
        
    def __repr__(self):
        return '<Workout %r>' % self.Name
        

class Workoutgroup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    workouts = db.relationship('Workout', backref='workout_group', lazy='dynamic')
    
    def __init__(self, name):
        self.Name = name

        
    def __repr__(self):
        return '<WorkoutGroup %r>' % self.Name