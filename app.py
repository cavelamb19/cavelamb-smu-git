from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms_is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Employee(db.Model):
    __tablename__ = 'employee'

    staffID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    Username = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    CurrentDesignation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    ContactNo = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'employee'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


    

class Learner(Employee):
    __tablename__ = 'learner'

    learnerID= db.Column(db.Integer, db.ForeignKey('employee.staffID'),primary_key=True)
    CoursesTaking = db.Column(db.String(50))
    CompletedCourses = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'learner'
    }

    
class Trainer(Employee):
    __tablename__ = 'trainer'

    trainerID= db.Column(db.Integer, db.ForeignKey('employee.staffID'),primary_key=True)
    coursesTeaching = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'trainer'
    }



class Administrator(Employee):
    __tablename__ = 'administrator'

    administratorID= db.Column(db.Integer, db.ForeignKey('employee.staffID'),primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }

    def __init__(self, administratorID):
        self.administratorID = administratorID
       

    def json(self):
        return {"administratorID": self.administratorID}

class Course(db.Model):

    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(50))
    courseDesc = db.Column(db.String(50))
    preRequisites = db.Column(db.String(50))
    classesID= db.Column(db.Integer, db.ForeignKey('classes.classesID'),primary_key=True)

    def __init__(self, courseID,courseName,courseDesc,preRequisites,classesID):
        self.courseID = courseID
        self.courseName = courseName
        self.courseDesc = courseDesc
        self.preRequisites = preRequisites
        self.classesID = classesID

       

    def json(self):
        return {"courseID": self.courseID, "courseName": self.courseName,
        "courseDesc": self.courseDesc, "preRequisites": self.preRequisites, "classesID": self.classesID}

class Classes(db.Model):

    __tablename__ = 'classes'

    classesID = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DATE)
    startTime = db.Column(db.TIMESTAMP)
    endDate = db.Column(db.DATE)
    endTime= db.Column(db.TIMESTAMP)
    classesSize = db.Column(db.Integer)
    trainerAssigned = db.Column(db.String(50))
    lessonID = db.Column(db.Integer, db.ForeignKey('lesson.lessonID'),primary_key=True)

    def __init__(self, classesID,startDate,startTime,endDate,endTime,classesSize,trainerAssigned,lessonID):
        self.classesID = classesID
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.classesSize = classesSize
        self.trainerAssigned = trainerAssigned
        self.lessonID = lessonID

       

    def json(self):
        return {"classesID": self.classesID, "startDate": self.startDate,
        "startTime": self.startTime, "endDate": self.endDate,
        "endTime": self.endTime,"classesSize": self.classesSize,"trainerAssigned": self.trainerAssigned,
        "lessonID": self.lessonID}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
