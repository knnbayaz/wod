from flask_sqlalchemy import SQLAlchemy
from ..ex50.manage import app



db = SQLAlchemy(app)

class Workout(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(50))
    GroupId = db.Column(db.Integer, db.ForeignKey('WorkoutGroup.Id'))
    
    group = db.relationship('WorkoutGroup', backref = db.backref('workouts', lazy = 'dynamic'))
    
    def __init__(self, name, group):
        self.Name = name
        self.GroupId = group.Id
        
    def __repr__(self):
        return '<Workout %r>' % self.Name
        

class WorkoutGroup(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(50))
    
    def __init__(self, name):
        self.Name = name

        
    def __repr__(self):
        return '<WorkoutGroup %r>' % self.Name